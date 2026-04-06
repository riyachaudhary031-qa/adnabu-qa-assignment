"""
home_page.py
------------
Page Object for the AdNabuTestStore Homepage.
Handles navigation and triggering the search flow.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class HomePage(BasePage):
    """
    Represents the store homepage.
    Primary responsibility: open the search modal and submit a search query.
    """

    # ------------------------------------------------------------------
    # Locators — update these if the store's HTML structure changes
    # ------------------------------------------------------------------

    # The search toggle button in the navbar (common in Shopify Dawn theme)
    SEARCH_TOGGLE_BTN = (By.CSS_SELECTOR, "button.search-modal__open-button, a[href*='search']")

    # The text input inside the search modal / search page
    SEARCH_INPUT = (By.CSS_SELECTOR, "input#Search-In-Modal-1, input[name='q'], input[type='search']")

    # Submit button inside the search form (fallback if Enter key doesn't work)
    SEARCH_SUBMIT_BTN = (By.CSS_SELECTOR, "button[type='submit'].search-modal__button, button[aria-label='Search']")

    # ------------------------------------------------------------------
    # Page Actions
    # ------------------------------------------------------------------

    def open_search_bar(self):
        """Click the search icon to open the search modal or navigate to search page."""
        self.click(*self.SEARCH_TOGGLE_BTN)

    def search_for(self, product_name: str):
        """
        Full search flow:
        1. Open search bar
        2. Type the product name
        3. Submit by pressing Enter
        """
        self.open_search_bar()
        self.type_text(*self.SEARCH_INPUT, product_name)
        # Press Enter to submit — more reliable than clicking a submit button
        self.find_visible(*self.SEARCH_INPUT).send_keys(Keys.RETURN)
