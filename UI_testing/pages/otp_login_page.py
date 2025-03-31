from playwright.sync_api import Page


class OtpLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://practice.expandtesting.com/otp-login"
        self.email_input = page.get_by_label("Your Email Address")
        self.button_send_otp_code = page.locator("#btn-send-otp")
        self.otp_input = page.locator("input#otp")
        self.button_verify_otp_code = page.locator("#btn-send-verify")

    def open(self):
        self.page.goto(self.url)
