import pytest
from playwright.sync_api import sync_playwright

from UI_testing.pages.browser_information_page import BrowserInformationPage
from UI_testing.pages.drag_and_drop_page import DragAndDropPage
from UI_testing.pages.input_page import InputPage
from UI_testing.pages.login_page import LoginPage
from UI_testing.pages.otp_login_page import OtpLoginPage
from UI_testing.pages.radio_button_page import RadioButtonPage
from UI_testing.pages.dynamic_table_page import DynamicTable
from UI_testing.pages.broken_images_page import BrokenImagePage

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


@pytest.fixture
def drag_and_drop_page(page):
    drag_and_drop = DragAndDropPage(page)
    drag_and_drop.open()
    return drag_and_drop

@pytest.fixture
def login_page(page):
    login_page = LoginPage(page)
    login_page.open()
    return login_page

@pytest.fixture
def otp_login_page(page):
    otp_login_page = OtpLoginPage(page)
    otp_login_page.open()
    return otp_login_page

@pytest.fixture
def radio_button_page(page):
    radio_button_page = RadioButtonPage(page)
    radio_button_page.navigate()
    return radio_button_page

@pytest.fixture
def browser_information_page(page):
    browser_information_page = BrowserInformationPage(page)
    browser_information_page.navigate()
    return browser_information_page

@pytest.fixture
def dynamic_table_page(page):
    dynamic_table_page = DynamicTable(page)
    dynamic_table_page.navigate()
    return dynamic_table_page

@pytest.fixture
def broken_image_page(page):
    broken_image_page = BrokenImagePage(page)
    broken_image_page.navigate()
    return broken_image_page

# це маленька фікстурка, яка наповнює сторінку якимись випадковими/дефолтними даними, щоб не вводити їх в тесті за потреби.
@pytest.fixture
def filled_input_page(input_page):
    input_page.number_input.fill("123")
    input_page.text_input.fill("Test text")
    input_page.password_input.fill("secretpassword")
    input_page.date_input.fill("2025-02-05")
    input_page.display_button.click()
    return input_page
@pytest.fixture
def filled_login_input(login_page: LoginPage):
    login_page.username.fill("practice")
    login_page.password.fill("SuperSecretPassword!")
    login_page.login_button.click()
    return login_page