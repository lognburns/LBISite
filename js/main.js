// Nav scroll state
const nav = document.querySelector('.nav');
const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 40);
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

// Mobile menu
const menuBtn = document.querySelector('.menu-btn');
const links = document.querySelector('.nav-links');
if (menuBtn) {
  menuBtn.addEventListener('click', () => {
    const open = links.classList.toggle('open');
    menuBtn.setAttribute('aria-expanded', open);
    menuBtn.textContent = open ? 'Close' : 'Menu';
  });
}

// Hero crossfade (homepage)
const heroDesktop = document.querySelector('.hero-slides--desktop');
const heroMobile = document.querySelector('.hero-slides--mobile');
const capTitle = document.querySelector('[data-hero-title]');
const capCat = document.querySelector('[data-hero-cat]');
const heroMq = window.matchMedia('(max-width: 860px)');
let heroTimer;

function activeHeroSlides() {
  if (heroMq.matches && heroMobile) return [...heroMobile.querySelectorAll('.hero-slide')];
  if (heroDesktop) return [...heroDesktop.querySelectorAll('.hero-slide')];
  return [...document.querySelectorAll('.hero-slide')];
}

function syncHeroCaption(slide) {
  if (capTitle && slide.dataset.title) capTitle.textContent = slide.dataset.title;
  if (capCat && slide.dataset.cat) capCat.textContent = slide.dataset.cat;
}

function setupHero() {
  clearInterval(heroTimer);
  const slides = activeHeroSlides();
  if (!slides.length) return;

  const active = slides.find((slide) => slide.classList.contains('on')) || slides[0];
  slides.forEach((slide) => slide.classList.toggle('on', slide === active));
  syncHeroCaption(active);

  if (slides.length < 2 || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  let i = slides.indexOf(active);
  heroTimer = setInterval(() => {
    slides[i].classList.remove('on');
    i = (i + 1) % slides.length;
    slides[i].classList.add('on');
    syncHeroCaption(slides[i]);
  }, 6000);
}

if (heroDesktop || heroMobile) {
  setupHero();
  heroMq.addEventListener('change', setupHero);
}

// Scroll reveals
const io = new IntersectionObserver((entries) => {
  entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach((el) => io.observe(el));

// Portfolio filters
const portfolioFilters = document.querySelectorAll('.portfolio-filter');
const portfolioCards = document.querySelectorAll('.grid-projects .card[data-type]');
if (portfolioFilters.length && portfolioCards.length) {
  portfolioFilters.forEach((btn) => {
    btn.addEventListener('click', () => {
      const filter = btn.dataset.filter;
      portfolioFilters.forEach((b) => {
        b.classList.toggle('on', b === btn);
        b.setAttribute('aria-selected', b === btn ? 'true' : 'false');
      });
      portfolioCards.forEach((card) => {
        card.classList.toggle('is-hidden', filter !== 'all' && card.dataset.type !== filter);
      });
    });
  });
}
