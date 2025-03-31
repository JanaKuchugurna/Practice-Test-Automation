from UI_testing.pages.drag_and_drop_page import DragAndDropPage


def test_drag_and_drop(drag_and_drop_page: DragAndDropPage):
    drag_and_drop_page.drag_circles_randomly()
    actual_order = drag_and_drop_page.get_order_in_square()
    assert actual_order == drag_and_drop_page.order, f"Expected order: {drag_and_drop_page.order}, reseived order: {actual_order}"


