from playwright.sync_api import expect

from UI_testing.pages.login_page import LoginPage


def test_valid_login_input(login_page: LoginPage):
    login_page.username.fill("practice")
    login_page.password.fill("SuperSecretPassword!")
    login_page.login_button.click()
    login_page.page.wait_for_url("https://practice.expandtesting.com/secure")
    expect(login_page.page).to_have_url("https://practice.expandtesting.com/secure")


def test_invalid_login_input(login_page: LoginPage):
    login_page.username.fill("wrong_user")
    login_page.password.fill("WrongPassword!")
    login_page.login_button.click()
    expect(login_page.page).to_have_url("https://practice.expandtesting.com/login")
    error_message = login_page.page.locator("#flash")
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("Your username is invalid!")