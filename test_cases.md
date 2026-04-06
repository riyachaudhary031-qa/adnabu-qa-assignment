# Test Cases — AdNabuTestStore
**Application:** AdNabuTestStore (E-commerce Web App)
**Prepared by:** QA Automation Engineer
**Date:** 2026-04-06

---

## Module 1: Product Search

---

### TC_PS_01 — Search with a Valid Product Name (Positive)

| Field          | Detail |
|----------------|--------|
| **Test Case ID** | TC_PS_01 |
| **Title**       | Search for a product using a valid, existing product name |
| **Preconditions** | Browser is open; user is on the AdNabuTestStore homepage |
| **Steps** | 1. Click the Search icon in the navigation bar <br> 2. Type a known product name (e.g., "Shirt") in the search input <br> 3. Press Enter or click the Search button |
| **Expected Result** | Search results page loads with at least one matching product displayed |

---

### TC_PS_02 — Search Results Display Product Details (Positive)

| Field          | Detail |
|----------------|--------|
| **Test Case ID** | TC_PS_02 |
| **Title**       | Verify product name and price are visible in search results |
| **Preconditions** | User has performed a valid product search (TC_PS_01 passed) |
| **Steps** | 1. Perform a search for "Shirt" <br> 2. Observe the search result cards |
| **Expected Result** | Each result card shows: product name, product image, and price |

---

### TC_PS_03 — Search with a Non-Existent Product Name (Negative)

| Field          | Detail |
|----------------|--------|
| **Test Case ID** | TC_PS_03 |
| **Title**       | Search for a product that does not exist in the store |
| **Preconditions** | Browser is open; user is on the homepage |
| **Steps** | 1. Click the Search icon <br> 2. Type "xyznonexistentproduct999" in the search input <br> 3. Press Enter |
| **Expected Result** | A "no results found" message is displayed; no products are listed |

---

### TC_PS_04 — Search with Empty Input (Negative)

| Field          | Detail |
|----------------|--------|
| **Test Case ID** | TC_PS_04 |
| **Title**       | Submit a search with an empty search field |
| **Preconditions** | Browser is open; user is on the homepage |
| **Steps** | 1. Click the Search icon <br> 2. Leave the input field blank <br> 3. Press Enter or click the Search button |
| **Expected Result** | Either the search is not submitted, or the user stays on the current page / sees a prompt to enter a search term. No crash or error page. |

---

### TC_PS_05 — Search with Special Characters (Edge Case)

| Field          | Detail |
|----------------|--------|
| **Test Case ID** | TC_PS_05 |
| **Title**       | Search using special characters to test input sanitisation |
| **Preconditions** | Browser is open; user is on the homepage |
| **Steps** | 1. Click the Search icon <br> 2. Type `<script>alert(1)</script>` in the search input <br> 3. Press Enter |
| **Expected Result** | The application handles the input gracefully — no JavaScript executes, no page error. Either shows "no results" or sanitised output. |

---

### TC_PS_06 — Search with Extremely Long String (Edge Case)

| Field          | Detail |
|----------------|--------|
| **Test Case ID** | TC_PS_06 |
| **Title**       | Search using a string exceeding typical character limits |
| **Preconditions** | Browser is open; user is on the homepage |
| **Steps** | 1. Click the Search icon <br> 2. Paste a 500-character string of random text into the input <br> 3. Press Enter |
| **Expected Result** | The application does not crash. Either truncates the input, shows "no results", or displays a validation message. Page remains functional. |

---

## Module 2: Add to Cart

---

### TC_AC_01 — Add a Single In-Stock Product to Cart (Positive)

| Field          | Detail |
|----------------|--------|
| **Test Case ID** | TC_AC_01 |
| **Title**       | Successfully add one in-stock product to the cart |
| **Preconditions** | User is on a product detail page; product is in stock |
| **Steps** | 1. Navigate to a product page <br> 2. Select required variant (size/colour) if applicable <br> 3. Click the "Add to Cart" button |
| **Expected Result** | Product is added to cart; cart icon count increments by 1; success notification or cart drawer appears |

---

### TC_AC_02 — Add Multiple Different Products to Cart (Positive)

| Field          | Detail |
|----------------|--------|
| **Test Case ID** | TC_AC_02 |
| **Title**       | Add two different products to the cart and verify both are present |
| **Preconditions** | User is on the homepage; both products are in stock |
| **Steps** | 1. Search for Product A and add it to the cart <br> 2. Navigate back to search <br> 3. Search for Product B and add it to the cart <br> 4. Open the cart |
| **Expected Result** | Cart contains both Product A and Product B; cart count shows 2 |

---

### TC_AC_03 — Attempt to Add an Out-of-Stock Product (Negative)

| Field          | Detail |
|----------------|--------|
| **Test Case ID** | TC_AC_03 |
| **Title**       | Verify that an out-of-stock product cannot be added to the cart |
| **Preconditions** | An out-of-stock product page is accessible |
| **Steps** | 1. Navigate to an out-of-stock product page <br> 2. Observe the Add to Cart button state |
| **Expected Result** | The "Add to Cart" button is disabled or replaced with "Sold Out"; clicking it has no effect |

---

### TC_AC_04 — Add Product Without Selecting a Required Variant (Negative)

| Field          | Detail |
|----------------|--------|
| **Test Case ID** | TC_AC_04 |
| **Title**       | Attempt to add a product to cart without selecting size/colour |
| **Preconditions** | User is on a product page that requires a variant selection (e.g., size) |
| **Steps** | 1. Navigate to a product with variants <br> 2. Do NOT select a size or colour <br> 3. Click "Add to Cart" |
| **Expected Result** | An error message appears prompting the user to select a variant. Product is NOT added to the cart. |

---

### TC_AC_05 — Add Product with Maximum Available Quantity (Edge Case)

| Field          | Detail |
|----------------|--------|
| **Test Case ID** | TC_AC_05 |
| **Title**       | Set product quantity to the maximum allowed and add to cart |
| **Preconditions** | User is on a product detail page with a quantity input field |
| **Steps** | 1. Navigate to a product page <br> 2. Change the quantity input to the maximum value (e.g., 99 or store max) <br> 3. Click "Add to Cart" |
| **Expected Result** | Product is added with the specified quantity OR the store enforces a quantity limit and displays a warning. No crash. |

---

### TC_AC_06 — Add the Same Product to Cart Multiple Times (Edge Case)

| Field          | Detail |
|----------------|--------|
| **Test Case ID** | TC_AC_06 |
| **Title**       | Add the same product twice and verify cart quantity aggregates correctly |
| **Preconditions** | User is on a product detail page; product is in stock |
| **Steps** | 1. Navigate to a product page <br> 2. Click "Add to Cart" <br> 3. Click "Add to Cart" again without changing quantity |
| **Expected Result** | Cart shows the same product with quantity 2 (not two separate line items), OR stores as two separate line items — behaviour must be consistent and no error shown |

---

*End of Test Cases Document*
