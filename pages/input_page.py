import time

from playwright.sync_api import Page


class InputPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://practice.expandtesting.com/inputs"

        self.number_input = page.get_by_label("Input: Number")  #TODO отак переробити всі лейби, просто за текстом
        self.text_input = page.locator('label:has-text("Input: Text")')
        self.password_input = page.locator('label:has-text("Input: Password")')
        self.date_input = page.locator('label:has-text("Input: Date")')

        self.display_button = page.get_by_role('button', name="Display Inputs")  #TODO отак переробити кнопки
        self.clear_button = page.locator('button:has-text("Clear Inputs")')

        self.output_number = page.locator('#output-number')
        self.output_text = page.locator('#output-text')
        self.output_password = page.locator('#output-password')
        self.output_date = page.locator('#output-date')

    def open(self):
        self.page.goto(self.url)

    # TODO позабирати отакі методи на одну стрічку, які нічого не роблять, ми в тесті спокійно взаємодіємо з елементами
    # внз включно з click_clear_button() я б забрала
    def enter_number(self, value: str):
        self.number_input.fill(value)

    def enter_text(self, value: str):
        self.text_input.fill(value)

    def enter_password(self, value: str):
        self.password_input.fill(value)

    def enter_date(self, value: str):
        self.date_input.fill(value)

    def click_display_button(self):
        self.display_button.click()

    def click_clear_button(self):
        self.clear_button.click()

    def get_input_values(self):
        return {
            "number": self.output_number.text_content().strip(),
            "text": self.output_text.text_content().strip(),
            "password": self.output_password.text_content().strip(),
            "date": self.output_date.text_content().strip()
        }

    # це має бути не тут, це ми готуємо об'єкт для порівняння, 
    # він не має бути в пейдж обджекті це раз, але й це не зовсім об'єкт, така штука має бути в тесті
    def check_clear_input(self):
        return {
            "number": self.number_input.input_value() == "",
            "text": self.text_input.input_value() == "",
            "password": self.password_input.input_value() == "",
            "date": self.date_input.input_value() == ""
        }

    def increase_value(self):
        self.number_input.press("ArrowUp")

    def decrease_value(self):
        self.number_input.press("ArrowDown")

    def get_number_value(self):
        return self.number_input.input_value()
