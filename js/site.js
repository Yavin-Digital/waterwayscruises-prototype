(function () {
  var banner = document.getElementById("proto-banner");
  function syncBanner() {
    if (!banner) return;
    document.documentElement.style.setProperty("--banner-h", banner.offsetHeight + "px");
  }
  syncBanner();
  window.addEventListener("resize", syncBanner);

  var header = document.querySelector(".site-header");
  if (header) {
    header.classList.add("is-solid");
    header.classList.remove("is-over-hero");
  }

  var finder = document.querySelector("[data-find]");
  if (finder) {
    finder.addEventListener("submit", function (event) {
      event.preventDefault();
      var data = new FormData(finder);
      var cruise = data.get("cruise");
      var routes = {
        dinner: "/dining-cruises/dinner/",
        brunch: "/dining-cruises/weekend-brunch-cruise/",
        supper: "/dining-cruises/supper/",
        seasonal: "/holiday-cruises/",
        private: "/request-a-proposal/"
      };
      var params = new URLSearchParams();
      if (data.get("date")) params.set("date", data.get("date"));
      if (data.get("party")) params.set("party", data.get("party"));
      var base = routes[cruise] || routes.dinner;
      if (cruise === "private") {
        window.location.href = base + (params.toString() ? "?" + params.toString() : "");
        return;
      }
      window.location.href = base + "?" + params.toString() + "#book";
    });
  }

  var query = new URLSearchParams(window.location.search);
  document.querySelectorAll("[data-book]").forEach(function (widget) {
    var date = widget.querySelector("[name='date']");
    var party = widget.querySelector("[name='party']");
    if (date && query.get("date")) date.value = query.get("date");
    if (party && query.get("party")) party.value = query.get("party");
  });
  var proposal = document.querySelector("#proposal");
  if (proposal && query.get("date")) {
    var when = proposal.querySelector("[name='date']");
    var guests = proposal.querySelector("[name='guests']");
    if (when) when.value = query.get("date");
    if (guests && query.get("party")) guests.value = query.get("party");
  }

  var toggle = document.getElementById("nav-toggle");
  var sheet = document.getElementById("nav-sheet");
  if (toggle && sheet) {
    toggle.addEventListener("click", function () {
      var open = sheet.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  document.querySelectorAll("form[data-preview]").forEach(function (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }
      var note = form.querySelector("[data-form-note]");
      if (note) {
        note.hidden = false;
        note.textContent = "Preview only. Nothing was sent, and no request was received.";
      }
    });
  });

  document.querySelectorAll("[data-book]").forEach(function (widget) {
    var steps = widget.querySelectorAll(".book-step");
    var labels = widget.querySelectorAll(".steps span");
    var index = 0;
    function show(next) {
      index = next;
      steps.forEach(function (step, i) {
        step.classList.toggle("on", i === index);
      });
      labels.forEach(function (label, i) {
        label.classList.toggle("on", i === index);
      });
      if (index === steps.length - 1) fillReview();
    }
    function val(name) {
      var el = widget.querySelector("[name='" + name + "']");
      return el ? el.value : "";
    }
    function fillReview() {
      var checks = [];
      widget.querySelectorAll("[data-enhance]:checked").forEach(function (box) {
        checks.push(box.value);
      });
      var target = widget.querySelector("[data-review]");
      if (!target) return;
      var cruise = val("cruise");
      var date = val("date");
      var party = val("party");
      target.innerHTML =
        "<p><strong>Preview selection.</strong> " +
        escapeHtml(cruise) +
        (date ? ", " + escapeHtml(date) : "") +
        (party ? ", party of " + escapeHtml(party) : "") +
        (checks.length ? ". Enhancements: " + escapeHtml(checks.join(", ")) + "." : ".") +
        "</p><p>No ticket was issued and no payment was taken.</p>";
    }
    widget.querySelectorAll("[data-next]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var current = steps[index];
        var fields = current.querySelectorAll("input, select, textarea");
        for (var i = 0; i < fields.length; i++) {
          if (!fields[i].checkValidity()) {
            fields[i].reportValidity();
            return;
          }
        }
        show(Math.min(index + 1, steps.length - 1));
      });
    });
    widget.querySelectorAll("[data-back]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        show(Math.max(index - 1, 0));
      });
    });
    show(0);
  });

  function escapeHtml(value) {
    return String(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }
})();
