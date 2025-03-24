import pytest
from playwright.sync_api import sync_playwright
from pages.input_page import InputPage


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        # browser = p.chromium.launch(headless=False, slow_mo=500)
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
    input_page.open()  #забрала перехід на сторінку на сторону пейджобджекта, щоб всі значення сторінки, включно з урллом зберігалися в одному місці
    return input_page

# це маленька фікстурка, яка наповнює сторінку якимись випадковими/дефолтними даними, щоб не вводити їх в тесті за потреби.
@pytest.fixture
def filled_input_page(input_page):
    input_page.enter_number("123")
    input_page.enter_text("Test text")
    input_page.enter_password("secretpassword")
    input_page.enter_date("2025-02-05")
    input_page.click_display_button()
    return input_page