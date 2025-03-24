import time
import pytest
from playwright.sync_api import sync_playwright
from UI_testing.pages.input_page import InputPage


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    time.sleep(5)
    page.close()


@pytest.fixture
def input_page(page):
    test_input_page = InputPage(page)
    page.goto("https://practice.expandtesting.com/inputs")
    return test_input_page
