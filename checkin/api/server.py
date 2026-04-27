"""FastAPI backend for the check-in web wizard.

Session state is in-memory (dict keyed by session id). Replace with redis/sqlite
if you need multi-worker or restart-persistent wizards. Each wizard step has a
dedicated endpoint under `/api/`.
"""
from __future__ import annotations

import csv
import json
import re
import uuid
from io import StringIO
from pathlib import Path
from typing import Any

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from .. import STAGING_DIR
from ..core import (
    bblock_index,
    bblock_match,
    bblock_writer,
    profile as profile_mod,
    sniff as sniff_mod,
    transformer_runner,
    vocab_index,
    vocab_match,
)

app = FastAPI(title="ILIAD check-in", version="0.1.0")

_WEB_DIR = Path(__file__).resolve().parent.parent / "web"

app.mount("/static", StaticFiles(directory=_WEB_DIR / "static"), name="static")

# Sessions
_SESSIONS: dict[str, dict[str, Any]] = {}
# Lazy caches built on first use
_BB_INDEX: list[bblock_index.BBlockEntry] | None = None
_VOCAB: vocab_index.VocabIndex | None = None


def _bb() -> list[bblock_index.BBlockEntry]:
    global _BB_INDEX
    if _BB_INDEX is None:
        _BB_INDEX = bblock_index.load_index()
    return _BB_INDEX


def _vocab() -> vocab_index.VocabIndex:
    global _VOCAB
    if _VOCAB is None:
        _VOCAB = vocab_index.build_index()
    return _VOCAB


@app.get("/", response_class=HTMLResponse)
def root() -> HTMLResponse:
    return HTMLResponse((_WEB_DIR / "index.html").read_text())


class RegisterIn(BaseModel):
    source: str


class RegisterOut(BaseModel):
    session_id: str
    sniff: dict
    profile: dict
    matches: list[dict]
    related: list[dict]


@app.post("/api/register", response_model=RegisterOut)
def register(body: RegisterIn) -> RegisterOut:
    s = sniff_mod.sniff(body.source)
    if s.format == "unknown":
        raise HTTPException(400, detail=f"cannot classify source: {s.hints}")
    p = profile_mod.profile(body.source, s.format)
    ranked = bblock_match.rank(p, _bb())  # all bblocks, sorted by score desc
    related = []  # populated after user picks a target
    sid = uuid.uuid4().hex[:12]
    _SESSIONS[sid] = {
        "source": body.source,
        "sniff": s.as_dict(),
        "profile": p.as_dict(),
        "matches": [
            {
                "id": m.entry.id,
                "title": m.entry.title,
                "score": m.score,
                "reason": m.reason,
                "matched_properties": m.matched_properties,
            }
            for m in ranked
        ],
    }
    return RegisterOut(
        session_id=sid,
        sniff=s.as_dict(),
        profile=p.as_dict(),
        matches=_SESSIONS[sid]["matches"],
        related=related,
    )


class ChooseBBlockIn(BaseModel):
    session_id: str
    bblock_id: str | None = None  # None => "generate new"


@app.post("/api/choose-bblock")
def choose_bblock(body: ChooseBBlockIn) -> dict:
    sess = _require_session(body.session_id)
    sess["chosen_bblock"] = body.bblock_id
    related_entries = bblock_match.related(body.bblock_id, _bb()) if body.bblock_id else []
    sess["related"] = [{"id": r.id, "title": r.title} for r in related_entries]
    return {"ok": True, "related": sess["related"]}


@app.get("/api/vocab-candidates/{session_id}")
def vocab_candidates(session_id: str) -> dict:
    sess = _require_session(session_id)
    profile = sess["profile"]
    props = [p["name"] for p in profile["properties"]]
    cands = vocab_match.match_properties(props, _vocab(), k=5)
    return {p: [c.as_dict() for c in cs] for p, cs in cands.items()}


class AcknowledgeIn(BaseModel):
    session_id: str
    mappings: dict[str, dict[str, str]]   # property_name -> {uri, label, source}


@app.post("/api/acknowledge-vocab")
def acknowledge_vocab(body: AcknowledgeIn) -> dict:
    sess = _require_session(body.session_id)
    sess["acknowledged_vocab"] = body.mappings
    return {"ok": True, "count": len(body.mappings)}


class ExternalLookupIn(BaseModel):
    query: str


@app.post("/api/external-vocab")
def external_vocab(body: ExternalLookupIn) -> dict:
    return {"hints": vocab_match.external_hints(body.query)}


class TransformersOut(BaseModel):
    candidates: list[dict]
    target_output: str | None


@app.get("/api/transformers/{session_id}", response_model=TransformersOut)
def transformers(session_id: str) -> TransformersOut:
    sess = _require_session(session_id)
    fmt = sess["sniff"]["format"]
    target_out_hint = {
        "csv": "stac-item",
        "tsv": "stac-item",
        "json": "geojson",
        "geojson": "geojson",
    }.get(fmt)
    specs = transformer_runner.find_matching(fmt, target_out_hint)
    # json-to-nested-json is universally available; surface it too.
    all_specs = transformer_runner.load_library()
    nested = next((s for s in all_specs if s.id == "json-to-nested-json"), None)
    if nested and nested not in specs:
        specs.append(nested)
    return TransformersOut(
        candidates=[s.as_dict() for s in specs],
        target_output=target_out_hint,
    )


@app.get("/api/mapping-suggestion/{session_id}")
def mapping_suggestion(session_id: str) -> dict:
    """Return target-bblock fields, source fields, and a best-guess mapping.

    Also returns the set of source fields NOT covered by any suggestion, as
    ``extras`` — the user names them and maps them to vocabularies so they
    become additional properties on the generated bblock.
    """
    from rapidfuzz import fuzz

    sess = _require_session(session_id)
    target_bb_id = sess.get("chosen_bblock")
    target_fields: list[dict] = []
    if target_bb_id:
        target = next((e for e in _bb() if e.id == target_bb_id), None)
        if target:
            target_fields = [tf.as_dict() for tf in target.target_fields]

    source_fields = [
        {"path": p["name"], "type": p["dtype"], "sample": p["sample_values"]}
        for p in sess["profile"]["properties"]
    ]

    # Suggestions — exact then fuzzy on last-segment of each path
    def leaf(path: str) -> str:
        return re.sub(r"\[\d*\]$", "", path.rsplit(".", 1)[-1])

    suggestions: list[dict] = []
    used_sources: set[str] = set()
    tgt_leaves = {tf["path"]: leaf(tf["path"]).lower() for tf in target_fields}
    for src in source_fields:
        sleaf = leaf(src["path"]).lower()
        if not sleaf:
            continue
        best_path = ""
        best_score = 0
        for tpath, tleaf in tgt_leaves.items():
            if not tleaf:
                continue
            score = 100 if sleaf == tleaf else fuzz.token_set_ratio(sleaf, tleaf)
            if score > best_score:
                best_score = score
                best_path = tpath
        if best_score >= 80 and best_path:
            suggestions.append({"source": src["path"], "target": best_path, "confidence": best_score})
            used_sources.add(src["path"])

    extras = [s for s in source_fields if s["path"] not in used_sources]
    return {
        "target_bblock": target_bb_id,
        "target_fields": target_fields,
        "source_fields": source_fields,
        "suggestions": suggestions,
        "extras": extras,
    }


class ExtraProp(BaseModel):
    source: str          # dotted path in source
    name: str            # name in new bblock (user-editable)
    uri: str = ""        # selected vocab URI
    label: str = ""
    source_src: str = ""  # bblock/ontology that defined the uri


class RunTransformerIn(BaseModel):
    session_id: str
    transformer_id: str
    params: dict[str, Any]


@app.post("/api/run-transformer")
def run_transformer(body: RunTransformerIn) -> dict:
    sess = _require_session(body.session_id)
    specs = transformer_runner.load_library()
    spec = next((s for s in specs if s.id == body.transformer_id), None)
    if spec is None:
        raise HTTPException(404, f"transformer {body.transformer_id} not found")
    sample = _prepare_sample(sess)
    result = transformer_runner.run(spec, sample, body.params)
    sess["transformer"] = {"id": spec.id, "params": body.params, "output": result.output}
    return {
        "ok": result.ok,
        "errors": result.errors,
        "validation_errors": result.validation_errors,
        "output_preview": _preview(result.output),
    }


class FinalizeIn(BaseModel):
    session_id: str
    bb_id: str
    title: str
    abstract: str = ""
    overwrite: bool = True
    extras: list[ExtraProp] = []   # user-named properties not in target bblock


@app.post("/api/finalize")
def finalize(body: FinalizeIn) -> dict:
    sess = _require_session(body.session_id)
    target_id = sess.get("chosen_bblock")
    target = next((e for e in _bb() if e.id == target_id), None) if target_id else None

    ack = sess.get("acknowledged_vocab") or {}
    mappings = [
        bblock_writer.AcknowledgedMapping(
            property_name=name, uri=info.get("uri", ""), label=info.get("label", ""), source=info.get("source", "")
        )
        for name, info in ack.items()
    ]

    tf_state = sess.get("transformer") or {}
    tf_spec = None
    if tf_state.get("id"):
        specs = transformer_runner.load_library()
        tf_spec = next((s for s in specs if s.id == tf_state["id"]), None)

    source_endpoint: dict[str, Any]
    source = sess["source"]
    source_endpoint = {"title": "source", "link": source} if sess["sniff"]["is_url"] else {
        "title": "source",
        "local_path": source,
    }

    # Add user-named extras as extra mapping entries with vocab URIs.
    extra_mappings = [
        bblock_writer.AcknowledgedMapping(
            property_name=e.name, uri=e.uri, label=e.label, source=e.source_src
        )
        for e in (body.extras or [])
        if e.name and e.uri
    ]

    draft = bblock_writer.BBlockDraft(
        id=body.bb_id,
        title=body.title,
        abstract=body.abstract or f"Auto-generated bblock from a {sess['sniff']['format']} source.",
        tags=[sess["sniff"]["format"], "checkin"],
        standards=(target.standards if target else []),
        depends_on=([target.id] if target else []),
        property_mappings=mappings + extra_mappings,
        extra_properties=[{"name": e.name, "source": e.source, "uri": e.uri} for e in (body.extras or [])],
        sample_feature=tf_state.get("output") or sess["profile"].get("sample"),
        source_endpoint=source_endpoint,
        transformer_kind="library" if tf_spec else "local",
        transformer=tf_spec,
        transformer_params=tf_state.get("params") or {},
    )
    target_path = bblock_writer.write_staged(draft, overwrite=body.overwrite)
    sess["staged_path"] = str(target_path)
    return {"ok": True, "staged_path": str(target_path)}


class PromoteIn(BaseModel):
    session_id: str
    bb_id: str


@app.post("/api/promote")
def promote(body: PromoteIn) -> dict:
    sess = _require_session(body.session_id)
    try:
        dest = bblock_writer.promote(body.bb_id)
    except (FileNotFoundError, FileExistsError) as exc:
        raise HTTPException(400, str(exc)) from exc
    sess["promoted_path"] = str(dest)
    return {"ok": True, "promoted_path": str(dest)}


# ---- helpers ----


def _require_session(sid: str) -> dict:
    sess = _SESSIONS.get(sid)
    if sess is None:
        raise HTTPException(404, f"unknown session {sid}")
    return sess


def _prepare_sample(sess: dict) -> Any:
    fmt = sess["sniff"]["format"]
    source = sess["source"]
    text = _fetch_text_safe(source)
    if fmt in {"csv", "tsv"} and text is not None:
        delim = "," if fmt == "csv" else "\t"
        return list(csv.DictReader(StringIO(text), delimiter=delim))
    if fmt in {"json", "geojson"} and text is not None:
        try:
            blob = json.loads(text)
        except json.JSONDecodeError:
            return {}
        if fmt == "geojson":
            return blob.get("features", [])
        return blob
    return sess["profile"].get("sample")


def _fetch_text_safe(source: str) -> str | None:
    try:
        if source.startswith(("http://", "https://")):
            with httpx.Client(follow_redirects=True, timeout=30.0) as c:
                r = c.get(source)
                r.raise_for_status()
                return r.text
        return Path(source).expanduser().read_text()
    except Exception:  # noqa: BLE001
        return None


def _preview(value: Any, limit: int = 3) -> Any:
    if isinstance(value, list):
        return value[:limit]
    return value


# ---- entrypoint ----


def main() -> None:  # pragma: no cover
    import uvicorn

    uvicorn.run("checkin.api.server:app", host="127.0.0.1", port=8000, reload=False)


if __name__ == "__main__":  # pragma: no cover
    main()
