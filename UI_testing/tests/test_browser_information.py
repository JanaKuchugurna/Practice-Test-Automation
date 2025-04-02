from playwright.sync_api import expect


def test_browser_info_visibility(browser_information_page):
    assert not browser_information_page.is_browser_info_visible(), "Browser info should be hidden initially"
    browser_information_page.hide_browser_information_button.click()
    expect(browser_information_page.browser_info).to_be_visible()
    browser_info = browser_information_page.get_browser_info()
    assert browser_info["user_agent"], "User Agent is empty"
    assert browser_info["code_name"], "Code Name is empty"
    assert browser_info["browser_name"], "Browser Name is empty"
    assert browser_info["version"], "Version is empty"
    assert browser_info["cookies_enabled"], "Cookies Enabled is empty"
    assert browser_info["platform"], "Platform is empty"
    browser_information_page.hide_browser_information_button.click()
    expect(browser_information_page.browser_info).not_to_be_visible()
