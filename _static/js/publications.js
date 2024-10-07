document.addEventListener("DOMContentLoaded", function () {
  const publicationList = document.getElementById("publication-list");
  const searchInput = document.getElementById("publication-search-input");
  const searchButton = document.getElementById("search-button");
  const resetButton = document.getElementById("reset-button");
  const prevButton = document.getElementById("prev-page");
  const nextButton = document.getElementById("next-page");
  const currentPageSpan = document.getElementById("current-page");
  const totalPagesSpan = document.getElementById("total-pages");

  const itemsPerPage = 11;
  let filteredItems = [...publicationList.children];
  let paginator = new Paginator(filteredItems, itemsPerPage);

  function updateDisplay() {
    paginator.showPage(paginator.currentPage);
    paginator.updatePageInfo(currentPageSpan, totalPagesSpan);
    paginator.updateButtonStates(prevButton, nextButton);
  }

  function handleSearch() {
    filteredItems = searchPublications();
    paginator = new Paginator(filteredItems, itemsPerPage);
    updateDisplay();
  }

  function handleReset() {
    filteredItems = resetSearch();
    paginator = new Paginator(filteredItems, itemsPerPage);
    updateDisplay();
  }

  searchButton.addEventListener("click", handleSearch);
  resetButton.addEventListener("click", handleReset);
  prevButton.addEventListener("click", () => {
    paginator.prevPage();
    updateDisplay();
  });
  nextButton.addEventListener("click", () => {
    paginator.nextPage();
    updateDisplay();
  });

  // Initial setup
  updateDisplay();
});
