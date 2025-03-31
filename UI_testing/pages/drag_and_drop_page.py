from random import shuffle
from playwright.sync_api import Page


class DragAndDropPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://practice.expandtesting.com/drag-and-drop-circles"
        self.drag_targ_square = page.locator("#target")
        self.circles = {
            "red": page.locator(".red"),
            "green": page.locator(".green"),
            "blue": page.locator(".blue"),
        }
        self.order = []

    def open(self):
        self.page.goto(self.url)

    def drag_circles_randomly(self):
        colors = list(self.circles.keys())
        shuffle(colors)
        self.order.clear()
        for color in colors:
            self.circles[color].drag_to(self.drag_targ_square)
            self.page.wait_for_selector("#target div", state="attached")
            self.order.append(color)

    def get_order_in_square(self):
        square_children = self.drag_targ_square.locator("div")
        count = square_children.count()
        order = [square_children.nth(i).get_attribute("class") for i in range(count)]
        print(f"Фактичний порядок елементів у квадраті: {order}")
        return order
