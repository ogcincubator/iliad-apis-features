(() => {
  const state = {
    sessionId: null,
    profile: null,
    matches: [],
    chosenBB: null,
    vocab: {},                  // property -> {uri,label,source}
    transformers: [],
    selectedTf: null,
    targetFields: [],
    sourceFields: [],
    suggestions: [],            // {source,target,confidence}
    extras: [],                 // user-editable; {source, name, uri, label, source_src, candidates}
  };

  const $ = (id) => document.getElementById(id);
  const activate = (id) => {
    document.querySelectorAll(".step").forEach((el) => el.classList.remove("active"));
    $(id).classList.add("active");
  };

  async function api(path, body) {
    const res = await fetch(path, {
      method: body ? "POST" : "GET",
      headers: body ? { "content-type": "application/json" } : {},
      body: body ? JSON.stringify(body) : undefined,
    });
    if (!res.ok) throw new Error(`${path}: ${res.status} ${await res.text()}`);
    return res.json();
  }

  // ---------- Step 1: register ----------
  $("btn-register").onclick = async () => {
    const src = $("source-input").value.trim();
    if (!src) return;
    $("register-output").textContent = "Detecting…";
    try {
      const r = await api("/api/register", { source: src });
      state.sessionId = r.session_id;
      state.profile = r.profile;
      state.matches = r.matches;
      $("register-output").textContent = JSON.stringify({ sniff: r.sniff, properties: r.profile.properties.map(p => p.name) }, null, 2);
      renderMatches(r.matches);
      activate("step-match");
    } catch (e) {
      $("register-output").textContent = "Error: " + e.message;
    }
  };

  function renderMatches(matches) {
    const root = $("matches");
    root.innerHTML = "";
    const filter = document.createElement("input");
    filter.type = "text";
    filter.placeholder = `Filter ${matches.length} building blocks…`;
    filter.className = "match-filter";
    root.appendChild(filter);

    const list = document.createElement("div");
    list.className = "match-list";
    root.appendChild(list);

    matches.forEach((m, i) => {
      const div = document.createElement("div");
      div.className = "match" + (i === 0 ? " selected" : "");
      div.dataset.id = m.id;
      div.dataset.search = `${m.id} ${m.title} ${(m.matched_properties || []).join(" ")}`.toLowerCase();
      div.innerHTML = `<span class="score">${m.score.toFixed(2)}</span> <strong>${m.id}</strong> — ${m.title}<br><span class="muted">${m.reason} · ${(m.matched_properties || []).slice(0, 6).join(", ")}</span>`;
      div.onclick = () => {
        document.querySelectorAll(".match").forEach(e => e.classList.remove("selected"));
        div.classList.add("selected");
      };
      list.appendChild(div);
    });
    const newDiv = document.createElement("div");
    newDiv.className = "match match-new";
    newDiv.dataset.id = "";
    newDiv.dataset.search = "generate new bblock";
    newDiv.innerHTML = `<strong>(generate new bblock — no existing one matches)</strong>`;
    newDiv.onclick = () => {
      document.querySelectorAll(".match").forEach(e => e.classList.remove("selected"));
      newDiv.classList.add("selected");
    };
    list.appendChild(newDiv);

    filter.oninput = () => {
      const q = filter.value.trim().toLowerCase();
      list.querySelectorAll(".match").forEach(el => {
        el.style.display = !q || el.dataset.search.includes(q) ? "" : "none";
      });
    };
  }

  // ---------- Step 2: choose bblock → vocab rows ----------
  $("btn-choose").onclick = async () => {
    const sel = document.querySelector(".match.selected");
    state.chosenBB = sel?.dataset.id || "";
    const r = await api("/api/choose-bblock", { session_id: state.sessionId, bblock_id: state.chosenBB || null });
    $("related").textContent = r.related.length ? "Related: " + r.related.map(x => x.id).join(", ") : "";
    const cands = await api(`/api/vocab-candidates/${state.sessionId}`);
    renderVocab(cands);
    activate("step-vocab");
  };

  function renderVocab(cands) {
    const root = $("vocab-rows");
    root.innerHTML = "";
    Object.entries(cands).forEach(([prop, list]) => {
      const row = document.createElement("div");
      row.className = "vocab-row";
      row.innerHTML = `<div><strong>${prop}</strong></div>`;
      const sel = document.createElement("select");
      sel.dataset.prop = prop;
      sel.innerHTML = `<option value="">— skip —</option>` + list.map((c, i) => `<option value="${i}">${(c.label || c.term)} · ${c.uri} (${c.source}, ${c.score})</option>`).join("");
      if (list.length > 0) sel.value = "0";
      row.appendChild(sel);
      root.appendChild(row);
      row.dataset.candidates = JSON.stringify(list);
    });
  }

  // ---------- Step 3: acknowledge vocab → transformer/mapping ----------
  $("btn-ack").onclick = async () => {
    const mappings = {};
    document.querySelectorAll(".vocab-row").forEach(row => {
      const sel = row.querySelector("select");
      if (!sel.value) return;
      const list = JSON.parse(row.dataset.candidates);
      const c = list[parseInt(sel.value, 10)];
      mappings[sel.dataset.prop] = { uri: c.uri, label: c.label, source: c.source };
    });
    state.vocab = mappings;
    await api("/api/acknowledge-vocab", { session_id: state.sessionId, mappings });

    // Load transformer list + mapping suggestion
    const t = await api(`/api/transformers/${state.sessionId}`);
    state.transformers = t.candidates;
    renderTransformers(t.candidates, t.target_output);

    const s = await api(`/api/mapping-suggestion/${state.sessionId}`);
    state.targetFields = s.target_fields;
    state.sourceFields = s.source_fields;
    state.suggestions = s.suggestions;
    state.extras = await enrichExtras(s.extras);
    renderMappingMatrix();
    renderExtras();
    activate("step-transformer");
  };

  async function enrichExtras(extras) {
    if (!extras || !extras.length) return [];
    // Fetch vocab candidates for each extra's leaf name via POST /api/acknowledge-vocab? We already have vocab candidates from step 3 for all source fields — reuse by refetching.
    const cands = await api(`/api/vocab-candidates/${state.sessionId}`);
    return extras.map(e => ({
      source: e.path,
      name: e.path.replace(/[^a-zA-Z0-9]+/g, "_").replace(/^_+|_+$/g, ""),
      candidates: cands[e.path] || [],
      chosen: 0,
    }));
  }

  // ---------- Step 4 render + run ----------
  function renderTransformers(list, targetOut) {
    const root = $("transformer-list");
    root.innerHTML = `<p class="muted">Target output: ${targetOut || "(multi-level via mapping)"}</p>`;
    list.forEach((t) => {
      const b = document.createElement("button");
      b.textContent = `${t.id} (${t.input} → ${t.output})`;
      b.onclick = () => selectTransformer(t);
      root.appendChild(b);
    });
    const preferred = list.find(t => t.id === "json-to-nested-json") || list[0];
    if (preferred) selectTransformer(preferred);
  }

  function selectTransformer(t) {
    state.selectedTf = t;
    const pp = $("transformer-params");
    pp.innerHTML = `<p class="muted">Params for <strong>${t.id}</strong></p>`;
    const props = (state.profile?.properties || []).map(p => p.name);
    const guesses = {
      lon_field: props.find(n => ["lon", "long", "longitude", "x"].includes(n.toLowerCase())) || "",
      lat_field: props.find(n => ["lat", "latitude", "y"].includes(n.toLowerCase())) || "",
      time_field: props.find(n => ["time", "datetime", "date", "timestamp", "eventdate", "observedon"].includes(n.toLowerCase())) || "",
      id_field: props.find(n => ["id", "uuid", "identifier"].includes(n.toLowerCase())) || "id",
    };
    const keys = t.id === "json-to-nested-json" ? [] : ["lon_field", "lat_field", "time_field", "id_field", "collection"];
    keys.forEach(k => {
      const lab = document.createElement("label");
      lab.textContent = k;
      const inp = document.createElement("input");
      inp.type = "text";
      inp.id = `param-${k}`;
      inp.value = guesses[k] || "";
      lab.appendChild(inp);
      pp.appendChild(lab);
    });
  }

  function renderMappingMatrix() {
    const root = $("mapping-matrix");
    root.innerHTML = "";
    if (!state.targetFields.length) {
      root.innerHTML = `<p class="muted">Target bblock exposes no enumerable fields; mapping skipped. The transformer will use inferred target paths.</p>`;
      return;
    }
    const sourceOpts = [`<option value="">— skip —</option>`]
      .concat(state.sourceFields.map(s => `<option value="${escapeAttr(s.path)}">${s.path}</option>`))
      .join("");
    state.targetFields.forEach(tf => {
      const sugg = state.suggestions.find(x => x.target === tf.path);
      const row = document.createElement("div");
      row.className = "mapping-row";
      row.dataset.target = tf.path;
      row.dataset.mode = "source";  // "source" | "expression"

      // Column 1: target info
      const tgtDiv = document.createElement("div");
      tgtDiv.className = "tgt";
      tgtDiv.innerHTML = `<code>${tf.path}</code><br><span class="muted">${tf.type || ""}${tf.example != null ? ` · e.g. ${JSON.stringify(tf.example).slice(0, 40)}` : ""}</span>`;
      row.appendChild(tgtDiv);

      // Column 2: mode toggle
      const modeBtn = document.createElement("button");
      modeBtn.className = "mode-toggle";
      modeBtn.textContent = "src";
      modeBtn.title = "Switch to expression mode";
      modeBtn.style.cssText = "padding:0.25rem 0.5rem;font-size:0.75rem;margin:0;";

      // Column 3: source select (shown in source mode)
      const sel = document.createElement("select");
      sel.dataset.target = tf.path;
      sel.innerHTML = sourceOpts;
      if (sugg) sel.value = sugg.source;
      sel.onchange = () => syncExtrasFromMatrix();

      // Column 3b: expression panel (hidden in source mode)
      const exprWrap = document.createElement("div");
      exprWrap.className = "expr-wrap";
      exprWrap.style.display = "none";

      const exprTa = document.createElement("textarea");
      exprTa.rows = 2;
      exprTa.placeholder = 'e.g. ${lon}  or  {"type":"Point","coordinates":[${lon},${lat}]}';
      exprTa.style.cssText = "width:100%;font-size:0.8rem;resize:vertical;";

      const pathLinks = document.createElement("div");
      pathLinks.className = "path-links";
      pathLinks.style.cssText = "font-size:0.75rem;margin-top:0.2rem;line-height:1.6;";
      state.sourceFields.forEach(sf => {
        const a = document.createElement("a");
        a.href = "#";
        a.textContent = sf.path;
        a.style.cssText = "margin-right:0.4rem;color:var(--muted);";
        a.onclick = (ev) => {
          ev.preventDefault();
          const ins = `\${${sf.path}}`;
          const pos = exprTa.selectionStart;
          exprTa.value = exprTa.value.slice(0, pos) + ins + exprTa.value.slice(exprTa.selectionEnd);
          exprTa.selectionStart = exprTa.selectionEnd = pos + ins.length;
          exprTa.focus();
        };
        pathLinks.appendChild(a);
      });
      exprWrap.appendChild(exprTa);
      exprWrap.appendChild(pathLinks);

      modeBtn.onclick = () => {
        const isExpr = row.dataset.mode === "expression";
        row.dataset.mode = isExpr ? "source" : "expression";
        modeBtn.textContent = isExpr ? "src" : "expr";
        modeBtn.title = isExpr ? "Switch to expression mode" : "Switch to source-path mode";
        sel.style.display = isExpr ? "" : "none";
        exprWrap.style.display = isExpr ? "none" : "";
        if (!isExpr) {
          // switching to expression: pre-fill from current select value
          const cur = sel.value;
          if (cur && !exprTa.value) exprTa.value = `\${${cur}}`;
          sel.value = "";
        }
        syncExtrasFromMatrix();
      };

      row.appendChild(modeBtn);
      row.appendChild(sel);
      row.appendChild(exprWrap);
      root.appendChild(row);
    });
    syncExtrasFromMatrix();
  }

  function usedSources() {
    const used = new Set();
    document.querySelectorAll("#mapping-matrix .mapping-row").forEach(row => {
      if (row.dataset.mode === "source") {
        const sel = row.querySelector("select");
        if (sel && sel.value) used.add(sel.value);
      } else {
        const ta = row.querySelector("textarea");
        if (ta) {
          const m = [...ta.value.matchAll(/\$\{([^}]+)\}/g)];
          m.forEach(match => used.add(match[1]));
        }
      }
    });
    return used;
  }

  function syncExtrasFromMatrix() {
    const used = usedSources();
    state.extras.forEach(e => { e._inUse = used.has(e.source); });
    renderExtras();
  }

  function renderExtras() {
    const root = $("extras-rows");
    root.innerHTML = "";
    const relevant = state.extras.filter(e => !e._inUse);
    if (!relevant.length) {
      root.innerHTML = `<p class="muted">No extras — every source field is mapped.</p>`;
      return;
    }
    relevant.forEach((e, idx) => {
      const row = document.createElement("div");
      row.className = "extra-row";
      row.innerHTML = `<div class="src"><code>${e.source}</code></div>`;
      const nameInp = document.createElement("input");
      nameInp.type = "text";
      nameInp.value = e.name;
      nameInp.placeholder = "name in new bblock";
      nameInp.oninput = () => { e.name = nameInp.value; };
      row.appendChild(nameInp);

      const sel = document.createElement("select");
      sel.innerHTML = `<option value="">— skip (don't include) —</option>` +
        e.candidates.map((c, i) => `<option value="${i}">${(c.label || c.term)} · ${c.uri} (${c.source}, ${c.score})</option>`).join("");
      if (e.candidates.length) { sel.value = String(e.chosen); }
      sel.onchange = () => { e.chosen = sel.value === "" ? null : parseInt(sel.value, 10); };
      row.appendChild(sel);
      root.appendChild(row);
    });
  }

  function collectMappings() {
    const mappings = [];
    document.querySelectorAll("#mapping-matrix .mapping-row").forEach(row => {
      const target = row.dataset.target;
      const targetField = state.targetFields.find(t => t.path === target);
      const type = (targetField && targetField.type) || "";
      if (row.dataset.mode === "expression") {
        const expr = row.querySelector("textarea")?.value.trim();
        if (expr) mappings.push({ expression: expr, target, type });
      } else {
        const sel = row.querySelector("select");
        if (sel && sel.value) mappings.push({ source: sel.value, target, type });
      }
    });
    return mappings;
  }

  function collectExtras() {
    return state.extras
      .filter(e => !e._inUse && e.chosen !== null && e.chosen !== undefined && e.name)
      .map(e => {
        const c = e.candidates[e.chosen];
        return {
          source: e.source,
          name: e.name,
          uri: c ? c.uri : "",
          label: c ? c.label : "",
          source_src: c ? c.source : "",
        };
      });
  }

  $("btn-run").onclick = async () => {
    if (!state.selectedTf) return;
    let params;
    if (state.selectedTf.id === "json-to-nested-json") {
      params = {
        target_template: {},
        mappings: collectMappings(),
        passthrough_extras: false,
        target_bblock: state.chosenBB || null,
      };
    } else {
      params = {};
      ["lon_field", "lat_field", "time_field", "id_field", "collection"].forEach(k => {
        const v = $(`param-${k}`)?.value;
        if (v) params[k] = v;
      });
    }
    $("transformer-output").textContent = "Running…";
    try {
      const r = await api("/api/run-transformer", {
        session_id: state.sessionId,
        transformer_id: state.selectedTf.id,
        params,
      });
      $("transformer-output").innerHTML = (r.ok ? '<span class="ok">OK</span>' : '<span class="err">FAIL</span>') +
        "\n" + JSON.stringify({ errors: r.errors, validation_errors: r.validation_errors, preview: r.output_preview }, null, 2);
      if (r.ok) activate("step-finalize");
    } catch (e) {
      $("transformer-output").textContent = "Error: " + e.message;
    }
  };

  $("btn-finalize").onclick = async () => {
    const body = {
      session_id: state.sessionId,
      bb_id: $("bb-id").value.trim(),
      title: $("bb-title").value.trim() || $("bb-id").value.trim(),
      abstract: $("bb-abstract").value.trim(),
      extras: collectExtras(),
    };
    if (!body.bb_id) { $("finalize-output").textContent = "bblock id is required"; return; }
    const r = await api("/api/finalize", body);
    $("finalize-output").textContent = JSON.stringify(r, null, 2);
  };

  $("btn-promote").onclick = async () => {
    const r = await api("/api/promote", { session_id: state.sessionId, bb_id: $("bb-id").value.trim() });
    $("promote-output").textContent = JSON.stringify(r, null, 2);
  };

  function escapeAttr(s) {
    return String(s).replace(/"/g, "&quot;").replace(/</g, "&lt;");
  }
})();
