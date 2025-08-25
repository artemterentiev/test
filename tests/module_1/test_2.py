import re
from playwright.sync_api import Page, expect

test_url = "https://practicesoftwaretesting.com/"
test_search_query = "hammer"
test_product_quantity = "3"

def test_2(page: Page) -> None:
    page.goto(test_url)
    page.locator("input[data-test=\"search-query\"]").fill(test_search_query)
    page.locator("button[data-test=\"search-submit\"]").click()
    page.locator("select[data-test=\"sort\"]").select_option("price,desc")
    page.locator(".card:nth-child(1)").click()

    product_name = page.locator("[data-test=\"product-name\"]").inner_text()
    product_price = page.locator("[data-test=\"unit-price\"]").inner_text()

    page.locator("input[data-test=\"quantity\"]").fill(test_product_quantity)
    page.locator("[data-test=\"add-to-cart\"]").click()
    # alert prevents to click the cart button. One of the possible ways is just to click on it to close.
    page.get_by_role("alert").click()
    page.locator("[data-test=\"nav-cart\"]").click()

    expect(page.locator("[data-test=\"product-title\"]")).to_contain_text(product_name)
    expect(page.locator("[data-test=\"product-quantity\"]")).to_have_value(test_product_quantity)
    expect(page.locator("[data-test=\"product-price\"]")).to_contain_text(product_price)
