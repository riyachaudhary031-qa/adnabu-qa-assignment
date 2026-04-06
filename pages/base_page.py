"""
base_page.py
------------
BasePage class that all page objects inherit from.
Contains reusable helper methods that wrap Selenium + WebDriverWait calls,
so we never use hardcoded sleeps anywhere in the project.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """
    Base class for all Page Objects.
    Provides common wait-based interactions (click, type, read text, visibility check).
    """

    DEFAULT_TIMEOUT = 10  # seconds

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    # ------------------------------------------------------------------
    # Core interaction helpers
    # ------------------------------------------------------------------

    def find_element(self, by, locator):
        """Wait until an element is present in the DOM, then return it."""
        return self.wait.until(
            EC.presence_of_element_located((by, locator)),
            message=f"Element not found: ({by}, {locator})"
        )

    def find_clickable(self, by, locator):
        """Wait until an element is visible AND clickable, then return it."""
        return self.wait.until(
            EC.element_to_be_clickable((by, locator)),
            message=f"Element not clickable: ({by}, {locator})"
        )

    def find_visible(self, by, locator):
        """Wait until an element is visible in the viewport, then return it."""
        return self.wait.until(
            EC.visibility_of_element_located((by, locator)),
            message=f"Element not visible: ({by}, {locator})"
        )

    def click(self, by, locator):
        """Wait for element to be clickable, then click it."""
        element = self.find_clickable(by, locator)
        element.click()

    def type_text(self, by, locator, text):
        """Wait for element, clear any existing text, then type new text."""
        element = self.find_visible(by, locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, by, locator):
        """Wait for element and return its visible text."""
        element = self.find_visible(by, locator)
        return element.text.strip()

    def is_visible(self, by, locator, timeout=5):
        """
        Check whether an element is visible within a given timeout.
        Returns True/False — does NOT raise an exception.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, locator))
            )
            return True
        except TimeoutException:
            return False

    def find_elements(self, by, locator):
        """
        Return a list of all matching elements (no wait — immediate).
        Useful for counting results or iterating over a list.
        """
        return self.driver.find_elements(by, locator)

    def get_current_url(self):
        """Return the current browser URL."""
        return self.driver.current_url
