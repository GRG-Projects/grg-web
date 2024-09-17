class Paginator {
  constructor(items, itemsPerPage) {
    this.items = items;
    this.itemsPerPage = itemsPerPage;
    this.currentPage = 1;
    this.totalPages = Math.ceil(this.items.length / this.itemsPerPage);
  }

  showPage(page) {
    const startIndex = (page - 1) * this.itemsPerPage;
    const endIndex = startIndex + this.itemsPerPage;

    this.items.forEach((item, index) => {
      item.style.display =
        index >= startIndex && index < endIndex ? "block" : "none";
    });

    this.currentPage = page;
  }

  nextPage() {
    if (this.currentPage < this.totalPages) {
      this.showPage(this.currentPage + 1);
    }
  }

  prevPage() {
    if (this.currentPage > 1) {
      this.showPage(this.currentPage - 1);
    }
  }

  updatePageInfo(currentPageSpan, totalPagesSpan) {
    currentPageSpan.textContent = this.currentPage;
    totalPagesSpan.textContent = this.totalPages;
  }

  updateButtonStates(prevButton, nextButton) {
    prevButton.disabled = this.currentPage === 1;
    nextButton.disabled = this.currentPage === this.totalPages;
  }
}
