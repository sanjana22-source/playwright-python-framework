import json
import time

import pytest
from playwright.sync_api import Playwright, expect

from Utils.APIUtil import APIUtils
from pageObjects.loginPage import LoginPage

with open("testData/credentials.json") as f:
    test_data = json.load(f)
    credentials= test_data["user_credentials"]


@pytest.mark.smoke
@pytest.mark.parametrize("user_credentials", credentials)
def test_orderConfirmation_web_api(playwright: Playwright, browserInstance, user_credentials):
    api_utils= APIUtils()
    order_id = api_utils.createOrder(playwright,user_credentials)
    username= user_credentials["userEmail"]
    password= user_credentials["userPassword"]
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    dashboardPage= loginPage.login(username,password)
    ordersPage= dashboardPage.selectOrdersNavLink()
    orderDetailsPage= ordersPage.selectOrder(order_id)
    orderDetailsPage.verifyOrderMessage()




