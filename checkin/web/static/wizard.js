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
    extras: [],                 // user-editable; {source, name, uri, label, source_src, candidates, mode, expression}
    vocabSources: [],
    stagedSourceId: null,       // set after finalize
    stagedTargetId: null,
  };

  const GEOM_TEMPLATES = [
    { label: "GeoJSON · Point",          expr: '{"type":"Point","coordinates":[${lon},${lat}]}' },
    { label: "GeoJSON · Point Z",        expr: '{"type":"Point","coordinates":[${lon},${lat},${depth}]}' },
    { label: "GeoJSON · BBox array",     expr: '[${west},${south},${east},${north}]' },
    { label: "GeoJSON · LineString",     expr: '{"type":"LineString","coordinates":[[${x1},${y1}],[${x2},${y2}]]}' },
    { label: "GeoJSON · Polygon",        expr: '{"type":"Polygon","coordinates":[[[${x1},${y1}],[${x2},${y2}],[${x3},${y3}],[${x1},${y1}]]]}' },
    { label: "WKT · Point",             expr: 'POINT(${lon} ${lat})' },
    { label: "WKT · Point Z",           expr: 'POINT Z(${lon} ${lat} ${depth})' },
    { label: "WKT · BBox / Envelope",   expr: 'POLYGON((${west} ${south},${east} ${south},${east} ${north},${west} ${north},${west} ${south}))' },
    { label: "WKT · LineString",        expr: 'LINESTRING(${x1} ${y1},${x2} ${y2})' },
    { label: "WKT · Polygon",          expr: 'POLYGON((${x1} ${y1},${x2} ${y2},${x3} ${y3},${x1} ${y1}))' },
  ];

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

  // ---------- Step 2: choose bblock → vocab source selection ----------
  $("btn-choose").onclick = async () => {
    const sel = document.querySelector(".match.selected");
    state.chosenBB = sel?.dataset.id || "";
    const r = await api("/api/choose-bblock", { session_id: state.sessionId, bblock_id: state.chosenBB || null });
    $("related").textContent = r.related.length ? "Related: " + r.related.map(x => x.id).join(", ") : "";
    const srcs = await api(`/api/vocab-sources/${state.sessionId}`);
    state.vocabSources = srcs.sources;
    renderVocabSources(srcs.sources);
    activate("step-vocab-sources");
  };

  // ---------- Step 3: vocab source configuration ----------
  function renderVocabSources(sources) {
    const root = $("vocab-source-list");
    root.innerHTML = "";
    sources.forEach((src, idx) => {
      const row = document.createElement("div");
      row.className = "source-row";
      row.dataset.sourceId = src.id;
      row.draggable = true;

      const cb = document.createElement("input");
      cb.type = "checkbox";
      cb.checked = src.enabled;
      cb.title = "Include this vocabulary in matching";
      cb.onchange = () => { src.enabled = cb.checked; };

      const info = document.createElement("div");
      info.className = "source-info";
      const badge = `<span class="prov-badge prov-${src.provenance}">${src.provenance}</span>`;
      const meta = [src.version, src.timestamp].filter(Boolean).join(" · ");
      info.innerHTML = `${badge} <strong>${src.label}</strong><br>
        <span class="muted">${src.uri}${meta ? ` · ${meta}` : ""} · ${src.term_count} terms</span>`;

      const btns = document.createElement("div");
      btns.className = "source-move-btns";
      const up = document.createElement("button");
      up.textContent = "↑";
      up.onclick = () => _moveSource(idx, -1);
      const dn = document.createElement("button");
      dn.textContent = "↓";
      dn.onclick = () => _moveSource(idx, +1);
      btns.appendChild(up);
      btns.appendChild(dn);

      row.appendChild(cb);
      row.appendChild(info);
      row.appendChild(btns);
      root.appendChild(row);

      // Drag-and-drop reorder
      row.addEventListener("dragstart", e => { e.dataTransfer.setData("text/plain", String(idx)); });
      row.addEventListener("dragover", e => { e.preventDefault(); row.classList.add("drag-over"); });
      row.addEventListener("dragleave", () => row.classList.remove("drag-over"));
      row.addEventListener("drop", e => {
        e.preventDefault();
        row.classList.remove("drag-over");
        const from = parseInt(e.dataTransfer.getData("text/plain"), 10);
        const to = idx;
        if (from !== to) {
          const moved = state.vocabSources.splice(from, 1)[0];
          state.vocabSources.splice(to, 0, moved);
          renderVocabSources(state.vocabSources);
        }
      });
    });
  }

  function _moveSource(idx, delta) {
    const newIdx = idx + delta;
    if (newIdx < 0 || newIdx >= state.vocabSources.length) return;
    const moved = state.vocabSources.splice(idx, 1)[0];
    state.vocabSources.splice(newIdx, 0, moved);
    renderVocabSources(state.vocabSources);
  }

  $("btn-load-custom-vocab").onclick = async () => {
    const url = $("custom-vocab-url").value.trim();
    if (!url) return;
    $("custom-vocab-status").textContent = "Loading…";
    try {
      const r = await api("/api/add-custom-vocab", { session_id: state.sessionId, url });
      state.vocabSources.push(r.source);
      renderVocabSources(state.vocabSources);
      $("custom-vocab-url").value = "";
      $("custom-vocab-status").textContent = `✓ ${r.source.term_count} terms loaded`;
    } catch (e) {
      $("custom-vocab-status").textContent = "Error: " + e.message;
    }
  };

  $("btn-confirm-sources").onclick = async () => {
    const priority = state.vocabSources.map(s => s.id);
    const disabled = state.vocabSources.filter(s => !s.enabled).map(s => s.id);
    await api("/api/configure-vocab-sources", {
      session_id: state.sessionId,
      source_priority: priority,
      disabled,
    });
    const cands = await api(`/api/vocab-candidates/${state.sessionId}`);
    renderVocab(cands);
    activate("step-vocab");
  };

  // ---- Vocab browser popup -------------------------------------------------

  let _vbResolve = null;   // called with {uri, label, source} when user picks
  let _vbDebounce = null;

  function showVocabBrowser() {
    const dlg = $("vocab-browser");
    dlg.hidden = false;
    dlg.showModal();
  }

  function hideVocabBrowser() {
    const dlg = $("vocab-browser");
    _vbResolve = null;
    if (dlg.open) dlg.close();
    dlg.hidden = true;
  }

  function openVocabBrowser(onPick) {
    _vbResolve = onPick;
    const dlg = $("vocab-browser");
    dlg.hidden = false;
    $("vb-search").value = "";
    $("vb-status").textContent = "";
    $("vb-list").innerHTML = "";
    showVocabBrowser();
    $("vb-search").focus();
    _loadVbTerms("");
  }

  async function _loadVbTerms(q) {
    $("vb-status").textContent = "Searching…";
    try {
      const r = await api(`/api/vocab-search/${state.sessionId}?q=${encodeURIComponent(q)}&limit=200`);
      $("vb-status").textContent = `${r.total_matched} match${r.total_matched !== 1 ? "es" : ""}${r.total_matched > 200 ? " (showing 200)" : ""}`;
      const list = $("vb-list");
      list.innerHTML = "";
      r.terms.forEach(t => {
        const div = document.createElement("div");
        div.className = "vb-term";
        div.innerHTML = `
          <div>
            <div class="vb-term-label">${escapeHtml(t.label || t.term)}</div>
            <div class="vb-term-uri">${escapeHtml(t.uri)}</div>
          </div>
          <div class="vb-term-src">${escapeHtml(t.source)}</div>`;
        div.onclick = () => {
          if (_vbResolve) _vbResolve({ uri: t.uri, label: t.label || t.term, source: t.source });
          hideVocabBrowser();
        };
        list.appendChild(div);
      });
    } catch (e) {
      $("vb-status").textContent = "Error: " + e.message;
    }
  }

  $("vb-search").oninput = () => {
    clearTimeout(_vbDebounce);
    _vbDebounce = setTimeout(() => _loadVbTerms($("vb-search").value.trim()), 250);
  };

  $("vb-close").onclick = () => hideVocabBrowser();
  $("vocab-browser").addEventListener("click", e => {
    if (e.target === $("vocab-browser")) hideVocabBrowser();
  });
  $("vocab-browser").addEventListener("close", () => {
    $("vocab-browser").hidden = true;
  });

  // ---- Render vocab rows ---------------------------------------------------

  function renderVocab(cands) {
    const root = $("vocab-rows");
    root.innerHTML = "";
    Object.entries(cands).forEach(([prop, list]) => {
      const row = document.createElement("div");
      row.className = "vocab-row";
      row.dataset.candidates = JSON.stringify(list);

      const label = document.createElement("div");
      label.innerHTML = `<strong>${prop}</strong>`;
      row.appendChild(label);

      const sel = document.createElement("select");
      sel.dataset.prop = prop;
      sel.innerHTML = `<option value="">— skip —</option>` +
        list.map((c, i) => `<option value="${i}">${escapeHtml((c.label || c.term))} · ${escapeHtml(c.uri)} (${escapeHtml(c.source)}, ${c.score})</option>`).join("");
      if (list.length > 0) sel.value = "0";
      row.appendChild(sel);

      // "Browse all…" button opens the popup
      const browseBtn = document.createElement("button");
      browseBtn.textContent = "Browse…";
      browseBtn.style.cssText = "padding:0.3rem 0.6rem;font-size:0.8rem;margin:0;background:#1e2330;color:var(--accent);";
      browseBtn.onclick = () => openVocabBrowser(picked => {
        const existing = Array.from(sel.options).find(o => o.dataset.uri === picked.uri);
        if (existing) {
          sel.value = existing.value;
        } else {
          const opt = document.createElement("option");
          const customIdx = `custom:${picked.uri}`;
          opt.value = customIdx;
          opt.dataset.uri = picked.uri;
          opt.dataset.label = picked.label;
          opt.dataset.source = picked.source;
          opt.textContent = `${picked.label} · ${picked.uri} (${picked.source})`;
          sel.appendChild(opt);
          const cList = JSON.parse(row.dataset.candidates);
          cList.push({ uri: picked.uri, label: picked.label, source: picked.source, term: picked.label, kind: "", score: 100 });
          row.dataset.candidates = JSON.stringify(cList);
          sel.value = customIdx;
        }
      });
      row.appendChild(browseBtn);
      root.appendChild(row);
    });
  }

  // ---------- Step 4: acknowledge vocab → transformer/mapping ----------
  $("btn-ack").onclick = async () => {
    const mappings = {};
    document.querySelectorAll(".vocab-row").forEach(row => {
      const sel = row.querySelector("select");
      if (!sel.value) return;
      const list = JSON.parse(row.dataset.candidates);
      if (sel.value.startsWith("custom:")) {
        const opt = sel.options[sel.selectedIndex];
        mappings[sel.dataset.prop] = { uri: opt.dataset.uri, label: opt.dataset.label, source: opt.dataset.source };
      } else {
        const c = list[parseInt(sel.value, 10)];
        mappings[sel.dataset.prop] = { uri: c.uri, label: c.label, source: c.source };
      }
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
    const cands = await api(`/api/vocab-candidates/${state.sessionId}`);
    return extras.map(e => ({
      source: e.path,
      name: e.path.replace(/[^a-zA-Z0-9]+/g, "_").replace(/^_+|_+$/g, ""),
      candidates: cands[e.path] || [],
      chosen: 0,
      mode: "source",
      expression: "",
    }));
  }

  // ---------- Step 5 render + run ----------
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

  // Build a geometry template <select> that inserts the chosen template into a textarea
  function makeGeomSelect(targetTa, onChange) {
    const sel = document.createElement("select");
    sel.innerHTML = `<option value="">— Geometry template… —</option>` +
      GEOM_TEMPLATES.map((t, i) => `<option value="${i}">${escapeHtml(t.label)}</option>`).join("");
    sel.style.cssText = "font-size:0.8rem;width:100%;margin-bottom:0.2rem;";
    sel.onchange = () => {
      if (!sel.value) return;
      targetTa.value = GEOM_TEMPLATES[parseFloat(sel.value, 10)].expr;
      if (onChange) onChange(targetTa.value);
      sel.value = "";
    };
    return sel;
  }

  // Build clickable field-path links that insert ${path} into a textarea
  function makePathLinks(targetTa, onChange) {
    const div = document.createElement("div");
    div.className = "path-links";
    div.style.cssText = "font-size:0.75rem;margin-top:0.2rem;line-height:1.6;";
    state.sourceFields.forEach(sf => {
      const a = document.createElement("a");
      a.href = "#";
      a.textContent = sf.path;
      a.style.cssText = "margin-right:0.4rem;";
      a.onclick = (ev) => {
        ev.preventDefault();
        const ins = `\${${sf.path}}`;
        const pos = targetTa.selectionStart;
        targetTa.value = targetTa.value.slice(0, pos) + ins + targetTa.value.slice(targetTa.selectionEnd);
        targetTa.selectionStart = targetTa.selectionEnd = pos + ins.length;
        if (onChange) onChange(targetTa.value);
        targetTa.focus();
      };
      div.appendChild(a);
    });
    return div;
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
      row.dataset.mode = "source";

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

      // Column 3a: source select (source mode)
      const sel = document.createElement("select");
      sel.dataset.target = tf.path;
      sel.innerHTML = sourceOpts;
      if (sugg) sel.value = sugg.source;
      sel.onchange = () => syncExtrasFromMatrix();

      // Column 3b: expression panel (expression mode)
      const exprWrap = document.createElement("div");
      exprWrap.className = "expr-wrap";
      exprWrap.style.display = "none";

      const exprTa = document.createElement("textarea");
      exprTa.rows = 2;
      exprTa.placeholder = 'e.g. ${lon}  or  {"type":"Point","coordinates":[${lon},${lat}]}';
      exprTa.style.cssText = "width:100%;font-size:0.8rem;resize:vertical;";

      exprWrap.appendChild(makeGeomSelect(exprTa));
      exprWrap.appendChild(exprTa);
      exprWrap.appendChild(makePathLinks(exprTa));

      modeBtn.onclick = () => {
        const isExpr = row.dataset.mode === "expression";
        row.dataset.mode = isExpr ? "source" : "expression";
        modeBtn.textContent = isExpr ? "src" : "expr";
        modeBtn.title = isExpr ? "Switch to expression mode" : "Switch to source-path mode";
        sel.style.display = isExpr ? "" : "none";
        exprWrap.style.display = isExpr ? "none" : "";
        if (!isExpr && !exprTa.value && sel.value) exprTa.value = `\${${sel.value}}`;
        if (!isExpr) sel.value = "";
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
          [...ta.value.matchAll(/\$\{([^}]+)\}/g)].forEach(m => used.add(m[1]));
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
    relevant.forEach((e) => {
      const row = document.createElement("div");
      row.className = "extra-row";

      // ---- Column 1: source control (select or expression) ----
      const srcWrap = document.createElement("div");
      srcWrap.className = "expr-wrap";

      // Mode toggle
      const modeBtn = document.createElement("button");
      modeBtn.textContent = e.mode === "source" ? "src" : "expr";
      modeBtn.style.cssText = "padding:0.2rem 0.4rem;font-size:0.7rem;margin:0 0 0.2rem 0;background:#1e2330;color:var(--muted);align-self:flex-start;";

      // Source-field select (all available source fields)
      const srcSel = document.createElement("select");
      srcSel.style.cssText = "font-size:0.8rem;width:100%;";
      srcSel.innerHTML = state.sourceFields
        .map(sf => `<option value="${escapeAttr(sf.path)}"${sf.path === e.source ? " selected" : ""}>${sf.path}</option>`)
        .join("");
      srcSel.style.display = e.mode === "source" ? "" : "none";
      srcSel.onchange = () => { e.source = srcSel.value; };

      // Expression textarea
      const exprTa = document.createElement("textarea");
      exprTa.rows = 2;
      exprTa.placeholder = 'e.g. ${depth_m}  or  {"type":"Point","coordinates":[${lon},${lat}]}';
      exprTa.style.cssText = "width:100%;font-size:0.8rem;resize:vertical;";
      exprTa.value = e.expression || "";
      exprTa.style.display = e.mode === "expression" ? "" : "none";
      exprTa.oninput = () => { e.expression = exprTa.value; };

      const geomSel = makeGeomSelect(exprTa, v => { e.expression = v; });
      geomSel.style.display = e.mode === "expression" ? "" : "none";

      const pathLinks = makePathLinks(exprTa, v => { e.expression = v; });
      pathLinks.style.display = e.mode === "expression" ? "" : "none";

      modeBtn.onclick = () => {
        const toExpr = e.mode === "source";
        e.mode = toExpr ? "expression" : "source";
        modeBtn.textContent = toExpr ? "expr" : "src";
        srcSel.style.display   = toExpr ? "none" : "";
        exprTa.style.display   = toExpr ? ""     : "none";
        geomSel.style.display  = toExpr ? ""     : "none";
        pathLinks.style.display = toExpr ? ""    : "none";
        if (toExpr && !exprTa.value && e.source) {
          exprTa.value = `\${${e.source}}`;
          e.expression = exprTa.value;
        }
      };

      srcWrap.appendChild(modeBtn);
      srcWrap.appendChild(srcSel);
      srcWrap.appendChild(geomSel);
      srcWrap.appendChild(exprTa);
      srcWrap.appendChild(pathLinks);
      row.appendChild(srcWrap);

      // ---- Column 2: name in new bblock ----
      const nameInp = document.createElement("input");
      nameInp.type = "text";
      nameInp.value = e.name;
      nameInp.placeholder = "name in new bblock";
      nameInp.oninput = () => { e.name = nameInp.value; };
      row.appendChild(nameInp);

      // ---- Column 3: vocabulary select ----
      const vocSel = document.createElement("select");
      vocSel.innerHTML = `<option value="">— skip (don't include) —</option>` +
        e.candidates.map((c, i) => `<option value="${i}">${(c.label || c.term)} · ${c.uri} (${c.source}, ${c.score})</option>`).join("");
      if (e.candidates.length && e.chosen !== null && e.chosen !== undefined) {
        vocSel.value = String(e.chosen);
      }
      vocSel.onchange = () => { e.chosen = vocSel.value === "" ? null : parseInt(vocSel.value, 10); };
      row.appendChild(vocSel);

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
      .filter(e => !e._inUse && e.name)
      .map(e => {
        const c = (e.chosen !== null && e.chosen !== undefined) ? e.candidates[e.chosen] : null;
        const base = {
          name: e.name,
          uri: c ? c.uri : "",
          label: c ? (c.label || c.term) : "",
          source_src: c ? c.source : "",
        };
        return e.mode === "expression"
          ? { ...base, expression: e.expression }
          : { ...base, source: e.source };
      });
  }

  $("btn-run").onclick = async () => {
    if (!state.selectedTf) return;
    let params;
    if (state.selectedTf.id === "json-to-nested-json") {
      // Include named extras as additional mappings so they appear in transformer output
      const extraMappings = state.extras
        .filter(e => !e._inUse && e.name)
        .map(e => e.mode === "expression" && e.expression
          ? { expression: e.expression, target: e.name }
          : e.source ? { source: e.source, target: e.name } : null
        ).filter(Boolean);
      params = {
        target_template: {},
        mappings: [...collectMappings(), ...extraMappings],
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

  // Live preview of the two bblock ids as user types
  $("bb-id").oninput = () => {
    const v = $("bb-id").value.trim() || "…";
    $("bb-id-preview-src").textContent = `${v}-source`;
    $("bb-id-preview-tgt").textContent = v;
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
    $("finalize-output").textContent = "Staging…";
    try {
      const r = await api("/api/finalize", body);
      state.stagedSourceId = r.source_id;
      state.stagedTargetId = r.target_id;
      $("finalize-output").textContent = [
        `✓ Staged ${r.source_id}  →  ${r.source_path}`,
        `✓ Staged ${r.target_id}  →  ${r.target_path}`,
      ].join("\n");
    } catch (e) {
      $("finalize-output").textContent = "Error: " + e.message;
    }
  };

  $("btn-promote").onclick = async () => {
    if (!state.stagedTargetId) { $("promote-output").textContent = "Stage first"; return; }
    $("promote-output").textContent = "Promoting…";
    try {
      const r = await api("/api/promote", { session_id: state.sessionId, bb_id: state.stagedTargetId });
      $("promote-output").textContent = r.promoted.map(p => `✓ ${p}`).join("\n");
    } catch (e) {
      $("promote-output").textContent = "Error: " + e.message;
    }
  };

  function escapeAttr(s) {
    return String(s).replace(/"/g, "&quot;").replace(/</g, "&lt;");
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }
})();
