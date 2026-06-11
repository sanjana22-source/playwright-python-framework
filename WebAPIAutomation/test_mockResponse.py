import time

import pytest
from playwright.sync_api import Page

fakePayloadOrderResponse= {"data":[],"message":"No Orders"}

def intercept_response(route):
    route.fulfill(
        json= fakePayloadOrderResponse
    )

@pytest.mark.smoke
def test_mock_network(page: Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/", intercept_response)
    page.get_by_placeholder("email@example.com").fill("sanjanaamrutansu90@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Automation@2026")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    time.sleep(2)
    text = page.get_by_text("You have No Orders to show at this time. Please Visit Back Us")
    print(text)


