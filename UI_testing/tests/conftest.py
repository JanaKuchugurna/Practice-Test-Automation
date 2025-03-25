import pytest
from playwright.sync_api import sync_playwright
from UI_testing.pages.input_page import InputPage


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture
def input_page(page):
    input_page = InputPage(page)
    input_page.open()
    return input_page


# це маленька фікстурка, яка наповнює сторінку якимись випадковими/дефолтними даними, щоб не вводити їх в тесті за потреби.
@pytest.fixture
def filled_input_page(input_page):
    input_page.number_input.fill("123")
    input_page.text_input.fill("Test text")
    input_page.password_input.fill("secretpassword")
    input_page.date_input.fill("2025-02-05")
    input_page.display_button.click()
    return input_page
