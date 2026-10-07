/* ============================================================
   LexiAI · UI behaviour
   No analysis logic lives here. This file only talks to the Flask
   proxy (/api/...), which forwards to the existing FastAPI backend.
   ============================================================ */
(function () {
  "use strict";

  var SAMPLE_TEXT =
    "This Agreement is entered into by Party A and Party B. Either party may terminate with 30 days notice. " +
    "Liability is limited to direct damages. Governed by California law.";

  var $ = function (id) { return document.getElementById(id); };

  var docText = $("docText");
  var analyzeBtn = $("analyzeBtn");
  var analyzeLabel = $("analyzeLabel");
  var alertBox = $("alertBox");
  var loading = $("loading");
  var results = $("results");
  var historyList = $("historyList");
  var clearAllBtn = $("clearAllBtn");
  var toastEl = $("toast");
  var lastResult = { summary: "", clauses: "", entities: "" };

  /* ---------- helpers ---------- */
  function show(el) { el.classList.remove("hidden"); }
  function hide(el) { el.classList.add("hidden"); }

  function toast(msg) {
    toastEl.textContent = msg;
    show(toastEl);
    clearTimeout(toast._t);
    toast._t = setTimeout(function () { hide(toastEl); }, 2200);
  }

  function showAlert(msg, type) {
    alertBox.textContent = msg;
    alertBox.className = "alert " + (type || "error");
  }
  function clearAlert() { alertBox.className = "alert hidden"; alertBox.textContent = ""; }

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text !== undefined) n.textContent = text;
    return n;
  }

  function updateCount() {
    var n = docText.value.length;
    $("charCount").textContent = n.toLocaleString() + " character" + (n === 1 ? "" : "s");
  }

  /* ---------- theme ---------- */
  $("themeBtn").addEventListener("click", function () {
    var root = document.documentElement;
    var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", next);
    try { localStorage.setItem("lexiai-theme", next); } catch (e) {}
  });

  /* ---------- mobile sidebar ---------- */
  var sidebar = $("sidebar"), backdrop = $("backdrop");
  function toggleSidebar(open) {
    sidebar.classList.toggle("open", open);
    backdrop.classList.toggle("hidden", !open);
  }
  $("menuBtn").addEventListener("click", function () { toggleSidebar(!sidebar.classList.contains("open")); });
  backdrop.addEventListener("click", function () { toggleSidebar(false); });

  /* ---------- editor ---------- */
  docText.addEventListener("input", updateCount);
  docText.addEventListener("keydown", function (e) {
    if ((e.ctrlKey || e.metaKey) && e.key === "Enter") { e.preventDefault(); analyze(); }
  });
  $("clearTextBtn").addEventListener("click", function () {
    docText.value = ""; updateCount(); clearAlert(); docText.focus();
  });
  $("loadSampleBtn").addEventListener("click", function () {
    docText.value = SAMPLE_TEXT; updateCount(); clearAlert();
    toggleSidebar(false);
    docText.focus();
  });

  /* ---------- rendering results ---------- */
  function renderClauses(text) {
    var box = $("clausesOut");
    box.innerHTML = "";
    var parsed = 0;
    String(text).split("\n").forEach(function (line) {
      var i = line.indexOf(":");
      if (i > 0 && i < 24) {
        var c = el("div", "clause");
        c.appendChild(el("div", "clause-label", line.slice(0, i).trim()));
        c.appendChild(el("div", "clause-text", line.slice(i + 1).trim() || "N/A"));
        box.appendChild(c);
        parsed++;
      }
    });
    if (!parsed) {
      var c2 = el("div", "clause");
      c2.appendChild(el("div", "clause-text", String(text)));
      box.appendChild(c2);
    }
  }

  function renderEntities(text) {
    var box = $("entitiesOut");
    box.innerHTML = "";
    var raw = String(text).trim();
    var parts = raw.split(/[,;\n]+/).map(function (s) { return s.trim(); }).filter(Boolean);
    if (parts.length <= 1 || raw === "N/A") {
      box.appendChild(el("span", "chip", raw || "N/A"));
      return;
    }
    parts.forEach(function (p) { box.appendChild(el("span", "chip", p)); });
  }

  function renderResults(data) {
    // Same fallbacks the Streamlit UI used
    var summary = data.summary !== undefined ? data.summary : (data.result !== undefined ? data.result : "N/A");
    var clauses = data.clauses !== undefined ? data.clauses : "N/A";
    var entities = data.entities !== undefined ? data.entities : "N/A";

    lastResult = { summary: String(summary), clauses: String(clauses), entities: String(entities) };
    $("summaryOut").textContent = lastResult.summary;
    renderClauses(lastResult.clauses);
    renderEntities(lastResult.entities);

    // restart entrance animation
    Array.prototype.forEach.call(results.querySelectorAll(".result-card"), function (c) {
      c.style.animation = "none"; void c.offsetWidth; c.style.animation = "";
    });
    show(results);
  }

  document.querySelectorAll(".copy-btn").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var key = btn.getAttribute("data-copy");
      var txt = lastResult[key] || "";
      if (navigator.clipboard) {
        navigator.clipboard.writeText(txt).then(function () { toast("Copied to clipboard"); });
      }
    });
  });

  /* ---------- analyze ---------- */
  function setBusy(busy) {
    analyzeBtn.disabled = busy;
    analyzeLabel.textContent = busy ? "Analyzing…" : "Analyze";
  }

  function analyze() {
    var text = docText.value;
    clearAlert();

    if (!text.trim()) {
      hide(results);
      showAlert("⚠️ Please paste a legal document", "warn");
      return;
    }

    hide(results);
    show(loading);
    setBusy(true);

    var body = new URLSearchParams();
    body.append("text", text);

    fetch("/api/analyze", { method: "POST", body: body })
      .then(function (r) {
        return r.json().catch(function () { return {}; }).then(function (data) { return { ok: r.ok, status: r.status, data: data }; });
      })
      .then(function (res) {
        if (res.ok) {
          renderResults(res.data);
          loadHistory(); // keep sidebar in sync with the new entry
        } else {
          showAlert("Error: " + (res.data && res.data.error ? res.data.error : res.status), "error");
        }
      })
      .catch(function (e) { showAlert("Error: " + e.message, "error"); })
      .then(function () { hide(loading); setBusy(false); });
  }
  analyzeBtn.addEventListener("click", analyze);

  /* ---------- history ---------- */
  function buildHistoryItem(item) {
    var wrap = el("div", "h-item");

    var head = el("button", "h-head");
    head.type = "button";
    head.appendChild(el("span", "", "🕒 " + item.timestamp));
    head.insertAdjacentHTML("beforeend",
      '<svg viewBox="0 0 24 24" class="ico chev"><path d="M6 9l6 6 6-6"/></svg>');
    head.addEventListener("click", function () { wrap.classList.toggle("open"); });

    var body = el("div", "h-body");
    var input = String(item.input_text || "");
    body.appendChild(el("div", "h-input", "Input: " + input.slice(0, 150) + "..."));

    var result = item.result || {};
    var summary = result.summary !== undefined ? result.summary : (result.result !== undefined ? result.result : "N/A");
    var s = el("div", "h-summary");
    s.appendChild(el("strong", "", "Summary: "));
    s.appendChild(document.createTextNode(String(summary)));
    body.appendChild(s);

    var actions = el("div", "h-actions");
    var loadBtn = el("button", "btn btn-ghost btn-sm", "↩️ Load");
    loadBtn.type = "button";
    loadBtn.addEventListener("click", function () {
      docText.value = input; updateCount(); clearAlert();
      toggleSidebar(false);
      docText.focus();
    });
    var delBtn = el("button", "btn btn-danger-ghost btn-sm", "🗑️ Delete");
    delBtn.type = "button";
    delBtn.addEventListener("click", function () {
      fetch("/api/history/" + encodeURIComponent(item.id), { method: "DELETE" })
        .then(loadHistory)
        .catch(function (e) { toast("Delete failed: " + e.message); });
    });
    actions.appendChild(loadBtn);
    actions.appendChild(delBtn);
    body.appendChild(actions);

    wrap.appendChild(head);
    wrap.appendChild(body);
    return wrap;
  }

  function loadHistory() {
    return fetch("/api/history")
      .then(function (r) {
        return r.json().then(function (data) {
          if (!r.ok) throw new Error(data && data.error ? data.error : r.status);
          return data;
        });
      })
      .then(function (history) {
        historyList.innerHTML = "";
        if (!history || !history.length) {
          historyList.appendChild(el("p", "muted small", "No past analyses yet."));
          hide(clearAllBtn);
          return;
        }
        history.slice(0, 10).forEach(function (item) { historyList.appendChild(buildHistoryItem(item)); });
        show(clearAllBtn);
      })
      .catch(function (e) {
        historyList.innerHTML = "";
        historyList.appendChild(el("p", "muted small", "Could not load history: " + e.message));
        hide(clearAllBtn);
      });
  }

  $("refreshHistoryBtn").addEventListener("click", function () { loadHistory().then(function () { toast("History refreshed"); }); });

  clearAllBtn.addEventListener("click", function () {
    if (!window.confirm("Delete all analysis history? This cannot be undone.")) return;
    fetch("/api/history", { method: "DELETE" })
      .then(loadHistory)
      .catch(function (e) { toast("Failed: " + e.message); });
  });

  /* ---------- init ---------- */
  updateCount();
  loadHistory();
})();
