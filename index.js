// --- Smooth scroll for anchor links ---
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// ---// Smooth scrolling for hero wave link
const waveLink = document.querySelector('.hero__wave a');
if (waveLink) {
    waveLink.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = waveLink.getAttribute('href');
        document.querySelector(targetId).scrollIntoView({ behavior: 'smooth' });
    });
}

// FAQ Accordion Logic
const faqToggles = document.querySelectorAll('.faq-toggle');

faqToggles.forEach(toggle => {
    toggle.addEventListener('click', () => {
        const content = toggle.nextElementSibling;
        const icon = toggle.querySelector('.faq-icon');
        const isOpen = content.style.maxHeight;

        // Close all other open accordions
        document.querySelectorAll('.faq-content').forEach(c => {
            c.style.maxHeight = null;
            c.style.paddingBottom = null;
        });
        document.querySelectorAll('.faq-icon').forEach(i => {
            i.style.transform = 'rotate(0deg)';
        });

        // Open this one if it wasn't already open
        if (!isOpen) {
            content.style.maxHeight = content.scrollHeight + 24 + "px"; // 24px for padding
            content.style.paddingBottom = "24px";
            icon.style.transform = 'rotate(180deg)';
        }
    });
});
