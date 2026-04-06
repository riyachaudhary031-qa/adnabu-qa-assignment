"""
product_page.py
---------------
Page Object for the Product Detail Page of AdNabuTestStore.
Handles reading product info and adding the product to the cart.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    """
    Represents an individual product detail page.
    Provides methods to read product details and interact with the cart.
    """

    # ------------------------------------------------------------------
    # Locators
    # ------------------------------------------------------------------

    # Product title on the detail page
    PRODUCT_TITLE = (By.CSS_SELECTOR, "h1.product__title, h1.product-single__title, h1")

    # Product price
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price__regular .price-item, .product__price, .price")

    # "Add to Cart" submit button
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[name='add'], form[action='/cart/add'] button[type='submit']")

    # Cart item count badge in the navbar (e.g., shows "1" after adding)
    CART_COUNT_BADGE = (By.CSS_SELECTOR, ".cart-count-bubble span, #cart-icon-bubble span[aria-hidden='true']")

    # Success notification or cart drawer that appears after adding
    SUCCESS_NOTIFICATION = (By.CSS_SELECTOR, ".cart-notification, .cart__notification, [id*='cart-notification']")

    # Cart drawer (slide-in panel shown after add)
    CART_DRAWER = (By.CSS_SELECTOR, "cart-drawer, .cart-drawer, #cart-drawer")

    # ------------------------------------------------------------------
    # Page Actions
    # ------------------------------------------------------------------

    def get_product_title(self) -> str:
        """Return the product name displayed on the page."""
        return self.get_text(*self.PRODUCT_TITLE)

    def get_product_price(self) -> str:
        """Return the product price displayed on the page."""
        return self.get_text(*self.PRODUCT_PRICE)

    def click_add_to_cart(self):
        """Click the 'Add to Cart' button."""
        self.click(*self.ADD_TO_CART_BTN)

    def is_add_to_cart_enabled(self) -> bool:
        """
        Return True if the 'Add to Cart' button is enabled (i.e., not disabled/sold-out).
        A disabled button usually means the product is out of stock.
        """
        btn = self.find_element(*self.ADD_TO_CART_BTN)
        return btn.is_enabled() and btn.get_attribute("disabled") is None

    def get_cart_count(self) -> int:
        """
        Return the integer value shown on the cart badge.
        Returns 0 if the badge is not visible.
        """
        if self.is_visible(*self.CART_COUNT_BADGE, timeout=5):
            text = self.get_text(*self.CART_COUNT_BADGE)
            return int(text) if text.isdigit() else 0
        return 0

    def is_cart_notification_visible(self) -> bool:
        """
        Return True if a cart success notification or cart drawer appeared
        after clicking Add to Cart.
        """
        return (
            self.is_visible(*self.SUCCESS_NOTIFICATION, timeout=5)
            or self.is_visible(*self.CART_DRAWER, timeout=5)
        )
