import time

from playwright.sync_api import Page, expect, Playwright


def test_launchBrowser(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/")


def test_shortcut_launch(page: Page):
    page.goto("https://rahulshettyacademy.com/")


def test_locators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    print(page.title())
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK21")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()

    page.get_by_role("button", name= "Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(5)

def test_firefoxBrowser(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    context = firefoxBrowser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    print(page.title())
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK21")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()

    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(5)


