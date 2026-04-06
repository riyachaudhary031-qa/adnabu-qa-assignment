# AdNabuTestStore — QA Automation Assignment

End-to-end automated tests for the **AdNabuTestStore** e-commerce web application.
Built with **Python + Selenium + pytest**, following the **Page Object Model (POM)** pattern.

---

## Project Structure

```
adnabu-qa-assignment/
│
├── conftest.py                     # Pytest fixtures (WebDriver setup/teardown)
├── pytest.ini                      # Pytest configuration
├── requirements.txt                # Project dependencies
│
├── pages/                          # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py                # Shared helper methods (wait, click, type)
│   ├── home_page.py                # Homepage — search bar interaction
│   ├── search_results_page.py      # Search results — reading & navigating results
│   └── product_page.py             # Product detail page — add to cart
│
├── tests/                          # Test scripts
│   ├── __init__.py
│   └── test_search_add_to_cart.py  # Main automated test scenario
│
├── reports/                        # Test report output (auto-generated)
│   └── sample_report.txt           # Sample expected output
│
└── test_cases.md                   # Manual test case documentation (12 test cases)
```

---

## Prerequisites

- Python 3.9 or higher
- Google Chrome browser (latest version)
- Internet connection (ChromeDriver is downloaded automatically)

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/adnabu-qa-assignment.git
cd adnabu-qa-assignment
```

### 2. Create and activate a virtual environment (recommended)

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> `webdriver-manager` automatically downloads the correct version of ChromeDriver.
> You do **not** need to install ChromeDriver manually.

---

## How to Run Tests

### Run all tests (default — verbose output)

```bash
pytest
```

### Run all tests with an HTML report

```bash
pytest --html=reports/report.html --self-contained-html
```

Open `reports/report.html` in any browser to view the formatted report.

### Run a specific test file

```bash
pytest tests/test_search_add_to_cart.py
```

### Run a specific test by name

```bash
pytest tests/test_search_add_to_cart.py::TestSearchAndAddToCart::test_search_product_and_add_to_cart
```

### Run tests headlessly (no visible browser window)

Uncomment this line in `conftest.py`:
```python
# options.add_argument("--headless=new")
```
Then run:
```bash
pytest
```

---

## Configuration

| Setting | Location | Default |
|---------|----------|---------|
| Store URL | `conftest.py → BASE_URL` | `https://adnabuteststore.myshopify.com` |
| Search term | `tests/test_search_add_to_cart.py → SEARCH_TERM` | `"Shirt"` |
| WebDriver timeout | `pages/base_page.py → DEFAULT_TIMEOUT` | `10` seconds |

If the store's HTML structure changes, update the **CSS locators** in the relevant page object file under `pages/`.

---

## Test Coverage

| Test ID | Description | Type |
|---------|-------------|------|
| TC_PS_01 | Search with valid product name | Positive |
| TC_PS_02 | Search results show product details | Positive |
| TC_PS_03 | Search for non-existent product | Negative |
| TC_PS_04 | Search with empty input | Negative |
| TC_PS_05 | Search with special characters | Edge Case |
| TC_PS_06 | Search with extremely long string | Edge Case |
| TC_AC_01 | Add single in-stock product to cart | Positive |
| TC_AC_02 | Add multiple products to cart | Positive |
| TC_AC_03 | Add out-of-stock product (should be blocked) | Negative |
| TC_AC_04 | Add product without selecting variant | Negative |
| TC_AC_05 | Add product with maximum quantity | Edge Case |
| TC_AC_06 | Add same product twice | Edge Case |

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.9+ | Programming language |
| Selenium 4 | Browser automation |
| pytest | Test runner & assertions |
| webdriver-manager | Auto ChromeDriver management |
| pytest-html | HTML test report generation |

---

## Design Decisions

- **Page Object Model (POM):** Each page of the app has its own class. This keeps test logic separate from UI interaction logic, making the code easy to maintain.
- **No hardcoded sleeps:** All waits use `WebDriverWait` with `expected_conditions`. This makes tests faster and more reliable.
- **`conftest.py` fixtures:** The WebDriver is set up and torn down automatically via a pytest fixture, so no setup/teardown boilerplate in each test.
- **`scope="function"` on driver fixture:** Every test gets a fresh browser instance, preventing state bleed between tests.

---

## Author

QA Automation Engineer — AdNabu Assignment
