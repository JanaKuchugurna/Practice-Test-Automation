from playwright.sync_api import Page


class BrokenImagePage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://practice.expandtesting.com/broken-images"
        self.image1 = page.get_by_alt_text("Image 1")
        self.image2 = page.get_by_alt_text("Image 1")
        self.image3 = page.get_by_alt_text("Image 3")

    def navigate(self):
        self.page.goto(self.url)

    def get_image_natural_width(self, image_locator) -> int:
        return image_locator.evaluate('el => el.naturalWidth')

    def is_image_broken(self, image_locator) -> bool:
        natural_width = self.get_image_natural_width(image_locator)
        return natural_width == 0
