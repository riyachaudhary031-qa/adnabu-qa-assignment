"""
search_results_page.py
----------------------
Page Object for the Search Results page of AdNabuTestStore.
Handles reading results and navigating to a product.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    """
    Represents the search results page after a query is submitted.
    Provides methods to read results and click into a product.
    """

    # ------------------------------------------------------------------
    # Locators
    # ------------------------------------------------------------------

    # Container shown when there are NO results
    NO_RESULTS_MSG = (By.CSS_SELECTOR, ".search__no-results, p.search-status__p, [data-empty-state]")

    # Individual product cards in the results grid
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".card-wrapper, .product-card-wrapper, li.grid__item")

    # Clickable link on the first product card (title or image)
    FIRST_PRODUCT_LINK = (By.CSS_SELECTOR, ".card__heading a, .card-wrapper a.full-unstyled-link, .product-card a")

    # Page heading (e.g., "Results for 'shirt'")
    PAGE_HEADING = (By.CSS_SELECTOR, "h1.search__title, h1, .search-status__p")

    # ------------------------------------------------------------------
    # Page Actions
    # ------------------------------------------------------------------

    def get_result_count(self) -> int:
        """Return the number of product cards visible on the results page."""
        cards = self.find_elements(*self.PRODUCT_CARDS)
        return len(cards)

    def has_results(self) -> bool:
        """Return True if at least one product card is displayed."""
        return self.get_result_count() > 0

    def is_no_results_shown(self) -> bool:
        """Return True if the 'no results' message is visible."""
        return self.is_visible(*self.NO_RESULTS_MSG)

    def click_first_product(self):
        """Click the first product in the search results to open its detail page."""
        self.click(*self.FIRST_PRODUCT_LINK)
