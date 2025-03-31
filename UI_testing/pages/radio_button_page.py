from playwright.sync_api import Page


class RadioButtonPage:
    def __init__(self, page: Page):
        self.page = page
        self.blue_radio_button = page.get_by_label("Blue")
        self.red_radio_button = page.get_by_label("Red")
        self.yellow_radio_button = page.get_by_label("Yellow")
        self.black_radio_button = page.get_by_label("Black")
        self.green_radio_button = page.locator("input#green")

    def navigate(self):
        self.page.goto("https://practice.expandtesting.com/radio-buttons")
