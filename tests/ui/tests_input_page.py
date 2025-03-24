from playwright.sync_api import expect
from pages.input_page import InputPage


def test_enter_valid_number(input_page: InputPage):
    input_page.enter_number("123")
    input_page.enter_text("Test text")
    input_page.enter_password("secretpassword")
    input_page.enter_date("2025-02-05")

    input_page.click_display_button()

    expect(input_page.output_number).to_have_text("123")
    expect(input_page.output_text).to_have_text("Test text")
    expect(input_page.output_password).to_have_text("secretpassword")
    expect(input_page.output_date).to_have_text("2025-02-05")


def test_invalid_input(input_page: InputPage):
    input_page.page.evaluate("document.querySelector('input[type=number]').value = 'abc'")
    actual_value = input_page.get_number_value()
    assert actual_value == "" or actual_value.isdigit(), f"Expected empty or number, but got '{actual_value}'"


def test_increase_number(input_page: InputPage):
    input_page.number_input.fill("10")  #тут цілком можна лишити звертання до елементу, бо абсолютно зрозуміло що відбувається
    input_page.increase_value()  #тут допустимо винести в функцію, бо взаємодія з елементом не зовсім очевидно і метод краще пояснює, що робиться
    assert input_page.get_number_value() == "11"


def test_decrease_number(input_page: InputPage):
    input_page.enter_number("10")
    input_page.decrease_value()
    assert input_page.get_number_value() == "9"

# отут ти перевіряєш функцію очищення, але чомусь асерти ще й на те, що все заповнилось правильно. 
# це значить в тебе тест виконує не одну функцію, значить на "все заповнилось правильно" - один тест,
# а на "все очистилось" - тільки чисте заповнення даних
def test_clear_input(input_page: InputPage):
    input_page.enter_number("123")
    input_page.enter_text("Test text")
    input_page.enter_password("secretpassword")
    input_page.enter_date("2025-02-05")
    input_page.click_display_button()

    input_values = input_page.get_input_values()

    assert input_values["number"].strip() == "123"
    assert input_values["text"].strip() == "Test text"
    assert input_values["password"].strip() == "secretpassword"
    assert input_values["date"].strip() == "2025-02-05"

    input_page.click_clear_button()

    clear_values = input_page.check_clear_input()
    assert clear_values["number"]
    assert clear_values["text"]
    assert clear_values["password"]
    assert clear_values["date"]

def test_clear_input_refactored(filled_input_page: InputPage):
    filled_input_page.click_clear_button()

    assert filled_input_page.number_input.input_value() == ""
    assert filled_input_page.text_input.input_value() == ""
    assert filled_input_page.password_input.input_value() == ""
    assert filled_input_page.date_input.input_value() == ""

#TODO треба розібратися, ще не мала часу
# def test_select_date_from_calendar(input_page: InputPage):
#     input_page.date_input.click()
#     input_page.page.locator("td:has-text('22')").click()
#     input_page.click_display_button()
#     assert input_page.output_date.text_content().strip() == "2025-03-22"
