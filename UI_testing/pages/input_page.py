from playwright.sync_api import Page


class InputPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://practice.expandtesting.com/inputs"

        self.number_input = page.get_by_label("Input: Number")
        self.text_input = page.get_by_label("Input: Text")
        self.password_input = page.get_by_label("Input: Password")
        self.date_input = page.get_by_label("Input: Date")

        self.display_button = page.get_by_role("button", name="Display Inputs")
        self.clear_button = page.get_by_role("button", name="Clear Inputs")

        self.output_number = page.locator("#output-number")
        self.output_text = page.locator("#output-text")
        self.output_password = page.locator("#output-password")
        self.output_date = page.locator("#output-date")

    def open(self):
        self.page.goto(self.url)

    def increase_value(self):
        self.number_input.press("ArrowUp")

    def decrease_value(self):
        self.number_input.press("ArrowDown")

    def get_number_value(self):
        return self.number_input.input_value()

