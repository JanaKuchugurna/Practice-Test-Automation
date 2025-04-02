from playwright.sync_api import Page


class BrowserInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://practice.expandtesting.com/my-browser"
        self.hide_browser_information_button = page.locator("#browser-toggle")
        self.browser_info = page.locator("#browser-info")
        self.user_agent = page.locator("#browser-user-agent")
        self.code_name = page.locator("#browser-code-name")
        self.browser_name = page.locator("#browser-name")
        self.version = page.locator("#browser-version")
        self.cookies_enabled = page.locator("#browser-cookie")
        self.platform = page.locator("#browser-platform")

    def navigate(self):
        self.page.goto(self.url)

    def is_browser_info_visible(self) -> bool:
        return self.browser_info.is_visible()

    def get_browser_info(self) -> dict:
        return {
            "user_agent": self.user_agent.text_content(),
            "code_name": self.code_name.text_content(),
            "browser_name": self.browser_name.text_content(),
            "version": self.version.text_content(),
            "cookies_enabled": self.cookies_enabled.text_content(),
            "platform": self.platform.text_content(),
        }
