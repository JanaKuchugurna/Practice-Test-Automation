from playwright.async_api import expect
from playwright.sync_api import expect
from UI_testing.pages.otp_login_page import OtpLoginPage


def test_valid_otp_email_input(otp_login_page: OtpLoginPage):
    otp_login_page.open()
    otp_login_page.email_input.fill("practice@expandtesting.com")
    otp_login_page.button_send_otp_code.click()
    otp_login_page.page.wait_for_selector("input#otp", timeout=5000)
    otp_login_page.otp_input.fill("214365")
    otp_login_page.button_verify_otp_code.click()
    otp_login_page.page.wait_for_url("https://practice.expandtesting.com/secure")
    expect(otp_login_page.page).to_have_url("https://practice.expandtesting.com/secure")


def test_invalid_otp_input(otp_login_page: OtpLoginPage):
    otp_login_page.open()
    otp_login_page.email_input.fill("practice@expandtesting.com")
    otp_login_page.button_send_otp_code.click()
    otp_login_page.page.wait_for_selector("input#otp", timeout=5000)
    otp_login_page.otp_input.fill("315265")
    otp_login_page.button_verify_otp_code.click()
    expect(otp_login_page.page).to_have_url("https://practice.expandtesting.com/otp-verification")
    error_message = otp_login_page.page.locator("#otp-message")
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("The provided OTP code is incorrect. Please check your code and try again.")


def test_invalid_email_input(otp_login_page: OtpLoginPage):
    otp_login_page.open()
    otp_login_page.email_input.fill("invalid-email")
    otp_login_page.button_send_otp_code.click()
    error_message = otp_login_page.page.locator(".invalid-feedback")
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("Please enter a valid email address.")