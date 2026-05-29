// modal.js
document.addEventListener("DOMContentLoaded", function () {
  const modal = document.querySelector(".modal");
  const modalContainer = document.querySelector(".modal-container");
  const closeButton = document.querySelector("#close-modal");
  const modalTitle = document.querySelector("#modal-title");
  const modalContent = document.querySelector("#modal-content");

  // Function to open the modal
  function openModal(type, content) {
    modalTitle.textContent = type.charAt(0).toUpperCase() + type.slice(1);
    modalContent.textContent = "";
    if (type === "bibtex") {
      modalContent.classList.add("bibtex-view");

      const copyBtn = document.createElement("button");
      copyBtn.className = "bibtex-copy";
      copyBtn.type = "button";
      copyBtn.textContent = "Copy";
      copyBtn.addEventListener("click", function () {
        navigator.clipboard.writeText(content.trim()).then(function () {
          copyBtn.textContent = "Copied!";
          setTimeout(function () {
            copyBtn.textContent = "Copy";
          }, 1500);
        });
      });

      const pre = document.createElement("pre");
      pre.className = "bibtex-block";
      pre.textContent = content.trim();

      modalContent.appendChild(copyBtn);
      modalContent.appendChild(pre);
    } else {
      modalContent.classList.remove("bibtex-view");
      modalContent.textContent = content;
    }
    modal.style.display = "flex";
    document.body.classList.add("modal-open");
  }

  // Function to close the modal
  function closeModal() {
    modal.style.display = "none";
    document.body.classList.remove("modal-open");
  }

  // Get all elements with class "modal-link"
  const modalLinks = document.getElementsByClassName("modal-link");

  // Add click event to all modal links
  for (let i = 0; i < modalLinks.length; i++) {
    modalLinks[i].addEventListener("click", function (event) {
      event.preventDefault();
      const type = this.getAttribute("data-type");
      const content = this.getAttribute("data-content");
      openModal(type, content);
    });
  }

  // Close the modal when clicking on the close button
  closeButton.addEventListener("click", closeModal);

  // Close the modal when clicking outside of it
  modal.addEventListener("click", function (event) {
    if (event.target === modal) {
      closeModal();
    }
  });

  // Prevent closing when clicking inside the modal container
  modalContainer.addEventListener("click", function (event) {
    event.stopPropagation();
  });

  // Prevent scrolling on the body when the modal is open
  modal.addEventListener(
    "touchmove",
    function (event) {
      event.preventDefault();
    },
    { passive: false }
  );

  // Allow scrolling within the modal content
  modalContent.addEventListener(
    "touchmove",
    function (event) {
      event.stopPropagation();
    },
    { passive: true }
  );
});
