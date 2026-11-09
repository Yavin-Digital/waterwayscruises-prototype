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
        seasonal: "/seasonal-cruises/",
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

  var offer = document.getElementById("offer-pop");
  if (offer) {
    var offerDialog = offer.querySelector(".offer-dialog");
    var offerForm = offer.querySelector("[data-offer]");
    var offerThanks = offer.querySelector("[data-offer-thanks]");
    var lastFocus = null;
    var offerOpen = false;
    function offerFocusable() {
      return Array.prototype.slice.call(
        offerDialog.querySelectorAll("button, a[href], input, select, textarea")
      ).filter(function (el) {
        return !el.disabled && el.offsetParent !== null;
      });
    }
    function closeOffer() {
      if (!offerOpen) return;
      offerOpen = false;
      offer.hidden = true;
      document.body.classList.remove("offer-open");
      if (lastFocus && lastFocus.focus) lastFocus.focus();
    }
    function openOffer() {
      if (offerOpen) return;
      try {
        if (sessionStorage.getItem("ww-offer-seen")) return;
        sessionStorage.setItem("ww-offer-seen", "1");
      } catch (err) {
        return;
      }
      offerOpen = true;
      window.clearTimeout(offerTimer);
      window.removeEventListener("scroll", onOfferScroll);
      lastFocus = document.activeElement;
      offer.hidden = false;
      document.body.classList.add("offer-open");
      var closer = offer.querySelector(".offer-x");
      if (closer) closer.focus();
    }
    var offerTimer = window.setTimeout(openOffer, 8000);
    function onOfferScroll() {
      var doc = document.documentElement;
      var max = doc.scrollHeight - window.innerHeight;
      if (max > 0 && window.scrollY / max >= 0.5) openOffer();
    }
    window.addEventListener("scroll", onOfferScroll, { passive: true });
    offer.addEventListener("click", function (event) {
      if (event.target.closest("[data-offer-close]")) closeOffer();
    });
    document.addEventListener("keydown", function (event) {
      if (!offerOpen) return;
      if (event.key === "Escape") {
        event.preventDefault();
        closeOffer();
        return;
      }
      if (event.key !== "Tab") return;
      var items = offerFocusable();
      if (!items.length) return;
      var first = items[0];
      var last = items[items.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    });
    if (offerForm) {
      offerForm.addEventListener("submit", function (event) {
        event.preventDefault();
        if (!offerForm.checkValidity()) {
          offerForm.reportValidity();
          return;
        }
        offerForm.hidden = true;
        if (offerThanks) offerThanks.hidden = false;
      });
    }
    window.addEventListener("pagehide", function () {
      window.clearTimeout(offerTimer);
    });
  }

  document.querySelectorAll(".bg-video").forEach(function (video) {
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var button = video.parentElement.querySelector(".video-pause");
    if (reduce) {
      video.removeAttribute("autoplay");
      video.pause();
      video.hidden = true;
      if (button) button.hidden = true;
      return;
    }
    function arm() {
      video.querySelectorAll("source[data-src]").forEach(function (source) {
        if (!source.getAttribute("src")) source.setAttribute("src", source.getAttribute("data-src"));
      });
      if (video.getAttribute("data-lazy") !== null) video.load();
    }
    function playWhenReady() {
      var pending = video.play();
      if (pending && pending.catch) pending.catch(function () {});
    }
    function sync() {
      if (!button) return;
      var paused = video.paused;
      button.textContent = paused ? "Play" : "Pause";
      button.setAttribute("aria-pressed", paused ? "true" : "false");
    }
    if (button) {
      button.addEventListener("click", function (event) {
        event.preventDefault();
        event.stopPropagation();
        if (video.paused) {
          arm();
          playWhenReady();
        } else video.pause();
        sync();
      });
    }
    video.addEventListener("play", sync);
    video.addEventListener("pause", sync);
    if (video.getAttribute("data-lazy") !== null) {
      if (!("IntersectionObserver" in window)) {
        arm();
        playWhenReady();
        return;
      }
      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) {
            video.pause();
            return;
          }
          arm();
          playWhenReady();
        });
      }, { rootMargin: "0px" });
      observer.observe(video);
    }
  });

  document.querySelectorAll("[data-season-filter]").forEach(function (button) {
    button.addEventListener("click", function () {
      var season = button.getAttribute("data-season-filter");
      document.querySelectorAll("[data-season-filter]").forEach(function (other) {
        other.classList.toggle("is-on", other === button);
      });
      document.querySelectorAll(".season-group").forEach(function (group) {
        group.hidden = season !== "all" && group.getAttribute("data-season") !== season;
      });
    });
  });

  document.querySelectorAll("[data-season-note]").forEach(function (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }
      form.hidden = true;
      var thanks = form.parentElement.querySelector("[data-season-thanks]");
      if (thanks) thanks.hidden = false;
    });
  });

  function escapeHtml(value) {
    return String(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }
})();
