from playwright.sync_api import expect
from UI_testing.pages.radio_button_page import RadioButtonPage


def test_radio_buttons_selection(radio_button_page: RadioButtonPage):
    radio_button_page.navigate()

    radio_button_page.red_radio_button.check()
    expect(radio_button_page.red_radio_button).to_be_checked()

    radio_button_page.blue_radio_button.check()
    expect(radio_button_page.blue_radio_button).to_be_checked()

    radio_button_page.yellow_radio_button.check()
    expect(radio_button_page.yellow_radio_button).to_be_checked()

    radio_button_page.black_radio_button.check()
    expect(radio_button_page.black_radio_button).to_be_checked()

    expect(radio_button_page.green_radio_button).to_be_disabled()


def test_only_one_radio_can_be_selected(radio_button_page: RadioButtonPage):
    radio_button_page.navigate()

    radio_button_page.red_radio_button.check()
    expect(radio_button_page.red_radio_button).to_be_checked()

    expect(radio_button_page.blue_radio_button).not_to_be_checked()
    expect(radio_button_page.yellow_radio_button).not_to_be_checked()
    expect(radio_button_page.black_radio_button).not_to_be_checked()


def test_click_on_label_selects_radio_button(radio_button_page: RadioButtonPage):
    radio_button_page.navigate()

    radio_button_page.page.locator("label[for='red']").click()
    expect(radio_button_page.red_radio_button).to_be_checked()
