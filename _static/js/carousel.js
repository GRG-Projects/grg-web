document.addEventListener("DOMContentLoaded", function () {
  new Splide("#splide", {
    type: "loop",
    perPage: 5, // Number of slides to show at once
    perMove: 1, // Number of slides to move per scroll
    padding: "5rem",
    focus: "center", // Center the active slide
    gap: "2rem", // Gap between slides
    pagination: true, // Disable pagination
    arrows: true, // Enable navigation arrows
    autoplay: true, // Enable auto-play
    interval: 2500, // Time between auto-slides
    breakpoints: {
      768: {
        perPage: 1, // Show 1 slide at a time on smaller screens
      },
    },
  }).mount();
});
