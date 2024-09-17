function searchPublications() {
  console.log("Search function called");
  const searchInput = document.getElementById("publication-search-input");
  const searchTerm = searchInput.value.toLowerCase();
  const publicationItems = document.querySelectorAll(".publication-item");

  let visibleItems = [];

  publicationItems.forEach((item) => {
    const title = item
      .querySelector(".publication-title")
      .textContent.toLowerCase();
    const authors = item
      .querySelector(".publication-description")
      .textContent.toLowerCase();
    const isMatch = title.includes(searchTerm) || authors.includes(searchTerm);

    if (isMatch) {
      visibleItems.push(item);
    }
    item.style.display = isMatch ? "block" : "none";
  });

  return visibleItems;
}

function resetSearch() {
  console.log("Reset function called");
  const searchInput = document.getElementById("publication-search-input");
  searchInput.value = "";
  const publicationItems = document.querySelectorAll(".publication-item");

  publicationItems.forEach((item) => {
    item.style.display = "block";
  });

  return Array.from(publicationItems);
}

// Remove the DOMContentLoaded event listener from here
