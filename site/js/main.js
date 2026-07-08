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
const slides = document.querySelectorAll('.hero-slide');
const capTitle = document.querySelector('[data-hero-title]');
const capCat = document.querySelector('[data-hero-cat]');
if (slides.length > 1 && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  let i = 0;
  setInterval(() => {
    slides[i].classList.remove('on');
    i = (i + 1) % slides.length;
    slides[i].classList.add('on');
    if (capTitle && slides[i].dataset.title) capTitle.textContent = slides[i].dataset.title;
    if (capCat && slides[i].dataset.cat) capCat.textContent = slides[i].dataset.cat;
  }, 6000);
}

// Scroll reveals
const io = new IntersectionObserver((entries) => {
  entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach((el) => io.observe(el));
