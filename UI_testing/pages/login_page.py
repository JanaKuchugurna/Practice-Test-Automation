from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://practice.expandtesting.com/login"
        self.username = page.get_by_label("Username")
        self.password = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.logout_button = page.locator("#Logout")

    def open(self):
        self.page.goto(self.url)
