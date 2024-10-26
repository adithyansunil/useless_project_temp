// script.js

// Smooth scroll to top when navigating back to home page
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("nav ul li a").forEach(link => {
      link.addEventListener("click", function(event) {
        event.preventDefault();
        const target = document.querySelector(this.getAttribute("href"));
        if (target) {
          window.scrollTo({
            top: target.offsetTop,
            behavior: "smooth"
          });
        }
      });
    });
  });