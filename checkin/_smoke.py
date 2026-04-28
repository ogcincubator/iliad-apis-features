"""Lightweight smoke test — imports + core paths that don't need pandas/pyarrow/xarray."""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from checkin.core import bblock_index, bblock_match, sniff, transformer_runner, vocab_index, vocab_match
from checkin.core import bblock_writer
from checkin.core.profile import Profile, PropertySpec


def test_sniff_csv_path():
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as f:
        f.write("id,lon,lat,time,species,count\n1,12.5,55.3,2026-03-12T10:05:00Z,Aurelia aurita,7\n")
        path = f.name
    r = sniff.sniff(path)
    assert r.format == "csv", r
    print("  sniff csv ok:", r.format)
    return path


def test_sniff_url_ogc():
    r = sniff._sniff_ogc_url("https://example.org/geoserver/wfs?service=WFS&request=GetCapabilities")
    assert r == "ogc-wfs", r
    print("  sniff ogc-wfs ok")


def test_bblock_index():
    entries = bblock_index.load_index()
    ids = [e.id for e in entries]
    assert "macroobservation" in ids, ids
    print(f"  bblock index loaded {len(entries)} bblocks; sample: {ids[:3]}")
    # Ensure property extraction worked for at least one
    macro = next(e for e in entries if e.id == "macroobservation")
    assert len(macro.properties) > 0, "no properties extracted"
    print(f"    macroobservation properties: {macro.properties[:6]}")
    return entries


def test_vocab_index():
    idx = vocab_index.build_index()
    s = vocab_index.summary(idx)
    print("  vocab index summary:", s)
    assert s["total"] > 0
    assert s["distinct_terms"] > 0
    return idx


def test_bblock_match(entries):
    p = Profile(format="csv", source="fake")
    p.properties = [PropertySpec(name=n) for n in ["species", "abundance", "depth_m", "salinity_psu", "lat", "lon", "time"]]
    ranked = bblock_match.rank(p, entries, k=5)
    print("  top matches:")
    for m in ranked[:3]:
        print(f"    {m.score:.3f} {m.entry.id} — {m.reason} — {m.matched_properties[:4]}")
    assert ranked[0].entry.id in {"macroobservation", "iliad-jellyfish-features"}, ranked[0].entry.id


def test_vocab_match(idx):
    cands = vocab_match.match_one("species", idx, k=3)
    print(f"  vocab 'species' candidates: {[(c.label or c.term, c.uri[:60]) for c in cands]}")


def test_transformer_json_to_geojson():
    lib = transformer_runner.load_library()
    spec = next(s for s in lib if s.id == "json-to-json-feature")
    rec = {"id": "obs-1", "longitude": 12.5, "latitude": 55.3, "species": "Aurelia aurita", "count": 7}
    result = transformer_runner.run(spec, rec, {"lon_field": "longitude", "lat_field": "latitude", "id_field": "id"})
    assert result.ok, result.errors + result.validation_errors
    assert result.output["type"] == "Feature"
    print(f"  json-to-json-feature ok; bbox-ish coords: {result.output['geometry']['coordinates']}")


def test_transformer_csv_to_stac():
    lib = transformer_runner.load_library()
    spec = next(s for s in lib if s.id == "csv-to-stac-item")
    row = {"id": "r1", "lon": "12.5", "lat": "55.3", "time": "2026-03-12T10:05:00Z", "species": "Aurelia aurita", "count": "7"}
    result = transformer_runner.run(spec, row, {"lon_field": "lon", "lat_field": "lat", "time_field": "time", "id_field": "id"})
    assert result.ok, result.errors + result.validation_errors
    out = result.output
    assert out["stac_version"] == "1.0.0"
    assert out["properties"]["datetime"] == "2026-03-12T10:05:00Z"
    print(f"  csv-to-stac-item ok: {out['id']}")


def test_transformer_netcdf_structure_to_json():
    lib = transformer_runner.load_library()
    spec = next(s for s in lib if s.id == "netcdf-structure-to-json")
    base = Path(__file__).resolve().parent / "transformers" / "netcdf-structure-to-json" / "tests"
    input_obj = json.loads((base / "input.json").read_text())
    params = json.loads((base / "params.json").read_text())
    result = transformer_runner.run(spec, input_obj, params)
    assert result.ok, result.errors + result.validation_errors
    out = result.output
    assert out["dataset"]["title"] == "Baltic demo dataset"
    assert out["axes"][0]["name"] == "time"
    assert out["measurements"][0]["id"] == "sea_water_temperature"
    print(f"  netcdf-structure-to-json ok: {len(out['measurements'])} measurements")


def test_transformer_json_to_nested_json_array_grouping():
    lib = transformer_runner.load_library()
    spec = next(s for s in lib if s.id == "json-to-nested-json")
    rec = {"species": "Aurelia aurita", "lon": 12.5, "lat": 55.3, "count": 7}
    params = {
        "target_template": {},
        "mappings": [
            {"source": "species", "target": "features[].properties.species", "type": "string"},
            {"source": "count", "target": "features[].properties.abundance_value", "type": "integer"},
            {"expression": '{"type":"Point","coordinates":[${lon},${lat}]}', "target": "features[].geometry", "type": "object"},
            {"expression": '"Feature"', "target": "features[].type", "type": "string"},
        ],
    }
    result = transformer_runner.run(spec, rec, params)
    assert result.ok, result.errors + result.validation_errors
    feat = result.output["features"][0]
    assert feat["properties"]["species"] == "Aurelia aurita"
    assert feat["properties"]["abundance_value"] == 7
    assert feat["geometry"]["type"] == "Point"
    print("  json-to-nested-json array grouping ok")


def test_transformer_json_to_nested_json_numeric_strings():
    lib = transformer_runner.load_library()
    spec = next(s for s in lib if s.id == "json-to-nested-json")
    rec = {"lon": "12,5", "lat": "55.3"}
    params = {
        "target_template": {},
        "mappings": [
            {"expression": '{"type":"Point","coordinates":[${lon},${lat}]}', "target": "geometry", "type": "object"},
        ],
    }
    result = transformer_runner.run(spec, rec, params)
    assert result.ok, result.errors + result.validation_errors
    coords = result.output["geometry"]["coordinates"]
    assert coords == [12.5, 55.3], coords
    print("  json-to-nested-json numeric strings ok")


def test_bblock_writer():
    ack = [bblock_writer.AcknowledgedMapping(property_name="species", uri="http://rs.tdwg.org/dwc/terms/scientificName", source="macroobservation")]
    from checkin import STAGING_DIR
    lib = transformer_runner.load_library()
    spec = next(s for s in lib if s.id == "csv-to-stac-item")
    draft = bblock_writer.BBlockDraft(
        id="smoke-test-bb",
        title="Smoke Test BB",
        abstract="Generated by smoke test.",
        tags=["csv", "checkin"],
        source_format="csv",
        depends_on=["macroobservation"],
        property_mappings=ack,
        source_property_mappings=ack,
        source_properties=[
            {"name": "species", "dtype": "object", "sample_values": ["Aurelia aurita"]},
            {"name": "lon", "dtype": "float64", "sample_values": [12.5]},
            {"name": "lat", "dtype": "float64", "sample_values": [55.3]},
        ],
        sample_feature={"type": "Feature", "geometry": {"type": "Point", "coordinates": [12.5, 55.3]}, "properties": {"species": "Aurelia aurita"}},
        source_endpoint={"title": "sample csv", "local_path": "/tmp/sample.csv"},
        transformer_kind="library",
        transformer=spec,
        transformer_params={"lon_field": "lon", "lat_field": "lat", "time_field": "time", "target_bblock": "macroobservation"},
    )
    src_dir, tgt_dir = bblock_writer.write_staged_pair(draft, overwrite=True)
    print(f"  staged source → {src_dir}")
    print(f"  staged target → {tgt_dir}")
    assert (src_dir / "bblock.json").exists()
    assert (src_dir / "schema.yaml").exists()
    assert (src_dir / "context.jsonld").exists()
    assert (tgt_dir / "bblock.json").exists()
    assert (tgt_dir / "context.jsonld").exists()
    assert (tgt_dir / "transforms.yaml").exists()
    assert (tgt_dir / "transforms" / "mapping.json").exists()
    mapping = json.loads((tgt_dir / "transforms" / "mapping.json").read_text())
    assert mapping["target_bblock"] == "ogc.hosted.iliad.api.features.macroobservation"
    # Check target dependsOn includes source bblock
    bb = json.loads((tgt_dir / "bblock.json").read_text())
    assert any("smoke-test-bb-source" in d for d in bb["dependsOn"])
    # Cleanup
    import shutil
    shutil.rmtree(src_dir)
    shutil.rmtree(tgt_dir)


if __name__ == "__main__":
    print("== sniff ==")
    csv_path = test_sniff_csv_path()
    test_sniff_url_ogc()
    print("== bblock index ==")
    entries = test_bblock_index()
    print("== vocab index ==")
    idx = test_vocab_index()
    print("== bblock match ==")
    test_bblock_match(entries)
    print("== vocab match ==")
    test_vocab_match(idx)
    print("== transformers ==")
    test_transformer_json_to_geojson()
    test_transformer_csv_to_stac()
    test_transformer_netcdf_structure_to_json()
    test_transformer_json_to_nested_json_array_grouping()
    test_transformer_json_to_nested_json_numeric_strings()
    print("== writer ==")
    test_bblock_writer()
    print("\nALL SMOKE TESTS PASSED")
