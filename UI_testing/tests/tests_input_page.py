from UI_testing.pages.input_page import InputPage


def test_enter_valid_number(input_page: InputPage):
    input_page.number_input.fill("123")
    input_page.text_input.fill("Test text")
    input_page.password_input.fill("secretpassword")
    input_page.date_input.fill("2025-02-05")

    input_page.display_button.click()

    assert input_page.output_number.text_content().strip() == "123"
    assert input_page.output_text.text_content().strip() == "Test text"
    assert input_page.output_password.text_content().strip() == "secretpassword"
    assert input_page.output_date.text_content().strip() == "2025-02-05"


def test_invalid_input(input_page: InputPage):
    input_page.page.evaluate("document.querySelector('input[type=number]').value = 'abc'")
    actual_value = input_page.number_input.input_value()
    assert actual_value == "" or actual_value.isdigit(), f"Expected empty or number, but got '{actual_value}'"


def test_increase_number(input_page: InputPage):
    input_page.number_input.fill("10")
    input_page.increase_value()
    assert input_page.get_number_value() == "11"


def test_decrease_number(input_page: InputPage):
    input_page.number_input.fill("10")
    input_page.decrease_value()
    assert input_page.get_number_value() == "9"


def test_clear_input_refactored(filled_input_page: InputPage):
    filled_input_page.clear_button.click()

    assert filled_input_page.number_input.input_value() == ""
    assert filled_input_page.text_input.input_value() == ""
    assert filled_input_page.password_input.input_value() == ""
    assert filled_input_page.date_input.input_value() == ""
