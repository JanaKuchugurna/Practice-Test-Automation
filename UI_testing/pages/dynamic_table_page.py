from playwright.sync_api import Page


class DynamicTable:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://practice.expandtesting.com/dynamic-table"
        self.chrome_row = page.locator("//table//tr[td[contains(text(),'Chrome')]]")
        self.chrome_cpu_label = page.locator("#chrome-cpu")

    def navigate(self):
        self.page.goto(self.url)

    def get_chrome_cpu_value(self) -> str:

        headers = self.page.locator("//table//th").all_text_contents()

        try:
            cpu_index = headers.index("CPU") + 1
        except ValueError:
            raise Exception("The 'CPU' column was not found in the table headers!")

        cpu_locator = self.chrome_row.locator(f"td:nth-child({cpu_index})")
        return cpu_locator.text_content().strip()

    def get_chrome_cpu_label(self) -> str:
        return self.chrome_cpu_label.text_content().replace("Chrome CPU: ", "").strip()
