import re
from playwright.sync_api import Page, expect

test_url = "https://testpages.eviltester.com/styled/validation/input-validation.html"
test_firstname = "testFirstName"
test_lastname = "testLastName"
test_age = "22"
test_country = "Belarus"
test_notes = "test notes"

def test_1(page: Page) -> None:
    page.goto(test_url)
    page.get_by_role("textbox", name="First name:").fill(test_firstname)
    page.get_by_role("textbox", name="Last name:").fill(test_lastname)
    page.get_by_role("spinbutton", name="Age:").fill(test_age)
    page.get_by_label("Country:").select_option(test_country)
    page.get_by_role("textbox", name="Notes:").fill(test_notes)
    page.get_by_role("button", name="Submit").click()
    expect(page.locator("#firstname-value")).to_contain_text(test_firstname)
    expect(page.locator("#surname-value")).to_contain_text(test_lastname)
    expect(page.locator("#age-value")).to_contain_text(test_age)
    expect(page.locator("#country-value")).to_contain_text(test_country)
    expect(page.locator("#notes-value")).to_contain_text(test_notes)
    