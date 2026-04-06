"""
test_search_add_to_cart.py
--------------------------
Automated test: "Search for a product and add it to cart successfully"

Flow:
  1. Open the AdNabuTestStore homepage
  2. Search for a known product (e.g., "Shirt")
  3. Verify search results appear
  4. Click the first result to open the product page
  5. Verify the product page loaded correctly
  6. Click "Add to Cart"
  7. Verify the cart was updated (count incremented or notification shown)

Uses:
  - Python + Selenium WebDriver
  - WebDriverWait (NO hardcoded sleeps)
  - Page Object Model (HomePage, SearchResultsPage, ProductPage)
  - pytest for test execution
"""

import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage


# -----------------------------------------------------------------------
# Test configuration — change SEARCH_TERM to any product that exists
# -----------------------------------------------------------------------
SEARCH_TERM = "Shirt"


class TestSearchAndAddToCart:
    """
    Test suite for the end-to-end Search → Add to Cart flow.
    """

    def test_search_product_and_add_to_cart(self, driver):
        """
        TC_MAIN_01: Search for a product and add it to the cart successfully.

        Steps:
            1. Search for SEARCH_TERM from the homepage
            2. Assert at least one result is returned
            3. Click the first result
            4. Assert product detail page loaded (title is not empty)
            5. Assert "Add to Cart" button is enabled
            6. Click "Add to Cart"
            7. Assert cart count > 0 OR a cart notification appeared
        """

        # ------------------------------------------------------------------
        # Step 1: Search for the product
        # ------------------------------------------------------------------
        home = HomePage(driver)
        home.search_for(SEARCH_TERM)

        # ------------------------------------------------------------------
        # Step 2: Verify search results are displayed
        # ------------------------------------------------------------------
        results = SearchResultsPage(driver)
        assert results.has_results(), (
            f"Expected search results for '{SEARCH_TERM}', but none were found."
        )
        print(f"\n✔ Search returned {results.get_result_count()} result(s) for '{SEARCH_TERM}'")

        # ------------------------------------------------------------------
        # Step 3: Click the first product in the results
        # ------------------------------------------------------------------
        results.click_first_product()

        # ------------------------------------------------------------------
        # Step 4: Verify we are on a product detail page
        # ------------------------------------------------------------------
        product = ProductPage(driver)
        product_title = product.get_product_title()
        assert product_title, "Product title should not be empty on the product page."
        print(f"✔ Opened product: '{product_title}'")

        # ------------------------------------------------------------------
        # Step 5: Verify the Add to Cart button is available (not sold out)
        # ------------------------------------------------------------------
        assert product.is_add_to_cart_enabled(), (
            f"'Add to Cart' button is disabled for product: '{product_title}'. "
            "Please use an in-stock product for this test."
        )

        # ------------------------------------------------------------------
        # Step 6: Add the product to the cart
        # ------------------------------------------------------------------
        product.click_add_to_cart()
        print("✔ Clicked 'Add to Cart'")

        # ------------------------------------------------------------------
        # Step 7: Verify the cart was updated
        # Check EITHER the cart count badge incremented OR a notification appeared
        # (Different Shopify themes behave slightly differently)
        # ------------------------------------------------------------------
        cart_updated = (
            product.get_cart_count() > 0
            or product.is_cart_notification_visible()
        )
        assert cart_updated, (
            "Cart was not updated after clicking 'Add to Cart'. "
            "Expected cart count > 0 or a cart notification to appear."
        )
        print(f"✔ Cart updated. Cart count: {product.get_cart_count()}")
        print("\n✅ Test PASSED: Product searched and added to cart successfully.")

    def test_search_returns_no_results_for_invalid_term(self, driver):
        """
        TC_MAIN_02: Search for a non-existent product — expect no results.

        This test verifies the negative path: the store handles a bad search gracefully.
        """

        invalid_term = "xyznonexistentproduct123abc"

        home = HomePage(driver)
        home.search_for(invalid_term)

        results = SearchResultsPage(driver)

        # Either zero product cards OR a "no results" message should be shown
        no_results = (
            not results.has_results()
            or results.is_no_results_shown()
        )
        assert no_results, (
            f"Expected no results for '{invalid_term}', but products were returned."
        )
        print(f"\n✔ Correctly showed no results for invalid search term: '{invalid_term}'")
        print("\n✅ Test PASSED: No results shown for non-existent product.")
