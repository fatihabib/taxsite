// Scroll animations
document.addEventListener('DOMContentLoaded', () => {
    const faders = document.querySelectorAll('.fade-up, .fade-in');

    const appearOptions = { threshold: 0.1, rootMargin: "0px 0px -50px 0px" };

    const appearOnScroll = new IntersectionObserver((entries, appearOnScroll) => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            entry.target.style.animationPlayState = 'running';
            appearOnScroll.unobserve(entry.target);
        });
    }, appearOptions);

    faders.forEach(fader => {
        fader.style.animationPlayState = 'paused';
        appearOnScroll.observe(fader);
    });
});
document.getElementById("nav-toggle").addEventListener("click", function() {
    document.getElementById("nav-menu").classList.toggle("active");
});