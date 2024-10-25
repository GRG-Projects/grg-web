// _static/js/custom-navbar.js
document.addEventListener("DOMContentLoaded", function () {
  const mobileNavbar = document.querySelector(".mobile-navbar");
  const menuToggle = document.querySelector(".menu-toggle");

  menuToggle.addEventListener("click", function () {
    mobileNavbar.classList.toggle("active");
  });

  // Close mobile menu when clicking outside
  document.addEventListener("click", function (event) {
    if (
      !mobileNavbar.contains(event.target) &&
      mobileNavbar.classList.contains("active")
    ) {
      mobileNavbar.classList.remove("active");
    }
  });
});
