"""
conftest.py
-----------
Pytest configuration and shared fixtures.
The `driver` fixture sets up and tears down a Chrome browser instance
for every test function automatically.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# -----------------------------------------------------------------------
# Store configuration — change BASE_URL if the store URL changes
# -----------------------------------------------------------------------
BASE_URL = "https://adnabuteststore.myshopify.com"


@pytest.fixture(scope="function")
def driver():
    """
    Pytest fixture: provides a configured Chrome WebDriver instance.

    - scope="function" → a fresh browser is created before EACH test
      and closed after, ensuring full test isolation.
    - Uses webdriver-manager to auto-download the correct ChromeDriver,
      so no manual driver setup is needed.
    """

    # Configure Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")           # Open maximised window
    options.add_argument("--disable-notifications")     # Block browser pop-ups
    options.add_argument("--disable-infobars")          # Hide "Chrome is controlled by automation" bar
    # Uncomment below line to run headless (no visible browser window):
    # options.add_argument("--headless=new")

    # Automatically download and use the correct ChromeDriver version
    service = Service(ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=service, options=options)

    # Navigate to the store homepage before handing control to the test
    chrome_driver.get(BASE_URL)

    yield chrome_driver  # ← test runs here

    # Teardown: always close the browser after the test, even if it fails
    chrome_driver.quit()
