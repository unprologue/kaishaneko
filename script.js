const yearEl = document.getElementById("year");

if (yearEl) {
  yearEl.textContent = String(new Date().getFullYear());
}

const brandLink = document.querySelector(".brand");

if (brandLink) {
  brandLink.addEventListener("click", (event) => {
    event.preventDefault();
    window.location.assign(`${window.location.pathname}${window.location.search}`);
  });
}


const hero = document.querySelector(".hero");
const heroImage = hero?.querySelector(".hero-visual img");

if (hero && heroImage) {
  let heroReady = false;
  const markHeroReady = () => {
    if (heroReady) return;
    heroReady = true;
    window.requestAnimationFrame(() => hero.classList.add("is-ready"));
  };

  const decodeHeroImage = () => {
    if (typeof heroImage.decode === "function") {
      heroImage.decode().catch(() => {}).then(markHeroReady);
      return;
    }
    markHeroReady();
  };

  if (heroImage.complete && heroImage.naturalWidth > 0) {
    decodeHeroImage();
  } else {
    heroImage.addEventListener("load", decodeHeroImage, { once: true });
    heroImage.addEventListener("error", markHeroReady, { once: true });
    window.setTimeout(markHeroReady, 1200);
  }
} else if (hero) {
  hero.classList.add("is-ready");
}

const revealTargets = [
  ".hero-copy",
  ".hero-copy > *",
  ".sec-wrap",
].flatMap((selector) => Array.from(document.querySelectorAll(selector)));

const uniqueRevealTargets = Array.from(new Set(revealTargets));

const applyStagger = (selector, stepMs) => {
  const elements = Array.from(document.querySelectorAll(selector));
  elements.forEach((el, index) => {
    el.style.setProperty("--reveal-delay", `${index * stepMs}ms`);
  });
};

applyStagger(".hero-copy > *", 110);

if (uniqueRevealTargets.length > 0) {
  uniqueRevealTargets.forEach((el) => {
    el.classList.add("reveal");
  });

  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      {
        threshold: 0.12,
        rootMargin: "0px 0px -8% 0px",
      }
    );

    uniqueRevealTargets.forEach((el) => observer.observe(el));
  } else {
    uniqueRevealTargets.forEach((el) => el.classList.add("is-visible"));
  }
}

// Back-to-top button after scrolling; mobile order bar once the hero is out of view.
const heroSection = document.querySelector(".hero");
const updateScrollState = () => {
  document.body.classList.toggle("is-scrolled", window.scrollY > 600);
};
updateScrollState();
window.addEventListener("scroll", updateScrollState, { passive: true });

if (heroSection && "IntersectionObserver" in window) {
  new IntersectionObserver(([entry]) => {
    document.body.classList.toggle("is-past-hero", !entry.isIntersecting);
  }).observe(heroSection);
}

// Sections with data-pc-scale="<max width>" show the 1440px PC layout scaled to the screen
// width at or below that width ("仕上げは、みんなの手で。" and "選べる6色・4サイズ").
const PC_LAYOUT_WIDTH = 1440;
const pcScaledSections = Array.from(document.querySelectorAll("[data-pc-scale]"));
const fitPcScaledSections = () => {
  const viewportWidth = document.documentElement.clientWidth;
  pcScaledSections.forEach((section) => {
    const scaled = viewportWidth <= Number(section.dataset.pcScale);
    section.classList.toggle("is-pc-scaled", scaled);
    section.style.zoom = scaled ? String(viewportWidth / PC_LAYOUT_WIDTH) : "";
  });
};
fitPcScaledSections();
window.addEventListener("resize", fitPcScaledSections);

// Order / estimate links: change the URLs here only. Every link marked
// data-order-link / data-estimate-link in index.html takes its href from these.
const ORDER_URL = "https://mp1vnh-e3.myshopify.com";
const ESTIMATE_URL = "mailto:hello@unprologue.jp?subject=" + encodeURIComponent("会社猫のお見積り・ご相談");
document.querySelectorAll("[data-order-link]").forEach((a) => {
  a.href = ORDER_URL;
});
document.querySelectorAll("[data-estimate-link]").forEach((a) => {
  a.href = ESTIMATE_URL;
});

// Gallery: enlarge the small case photos in a <dialog>.
const lightbox = document.getElementById("lightbox");
if (lightbox && typeof lightbox.showModal === "function") {
  const lightboxImg = lightbox.querySelector("img");
  document.querySelectorAll(".case-thumb").forEach((button) => {
    button.addEventListener("click", () => {
      lightboxImg.src = button.dataset.full;
      lightboxImg.alt = button.dataset.alt || "";
      lightbox.showModal();
    });
  });
  lightbox.querySelector(".lightbox-close").addEventListener("click", () => lightbox.close());
  // a click on the backdrop (outside the photo) closes it
  lightbox.addEventListener("click", (event) => {
    if (event.target === lightbox) lightbox.close();
  });
}
