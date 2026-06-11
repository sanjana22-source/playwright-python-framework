import time

import pytest
from playwright.sync_api import Page, expect


def test_UIValidationDynamicScript(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    print(page.title())
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    iphoneProduct= page.locator("app-card").filter(has_text = 'iphone X')
    iphoneProduct.get_by_role("button", name = 'Add ').click()
    nokiaProduct= page.locator("app-card").filter(has_text = 'Nokia Edge')
    nokiaProduct.get_by_role("button", name = 'Add ').click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)


def test_childWindowHandle(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newPage_info:
        page.get_by_role("link", name="Free Access to InterviewQues/").click()
        childPage = newPage_info.value
        text = childPage.locator(".red").text_content()
        words= text.split("at")
        email = words[1].strip().split(" ")[0]
        print(email)
        assert email == "mentor@rahulshettyacademy.com"


@pytest.mark.regression
def test_handle_mousehover(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    page.get_by_role("link", name= "Top").click()
    time.sleep(4)


@pytest.mark.regression
@pytest.mark.smoke
def test_handleAlert(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.get_by_placeholder("Enter Your Name").fill("sanjana")
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="confirm").click()
    time.sleep(5)

def test_handleFrames(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    pageFrame= page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name = "All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers!")


def test_handle_webtable(page: Page):
    pass


