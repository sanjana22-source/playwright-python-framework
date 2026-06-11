import json

from playwright.sync_api import Playwright

payload= {
    "orders": [
        {
            "country": "India",
            "productOrderedId": "6960eac0c941646b7a8b3e68"
        }
    ]
}



class APIUtils:


    def get_token(self,playwright: Playwright,user_credentials):
        api_request_context= playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response= api_request_context.post(url="/api/ecom/auth/login",
                                           data = {"userEmail": user_credentials["userEmail"],"userPassword": user_credentials["userPassword"]},
                                           )

        assert response.ok
        response_body= response.json()
        token= response_body["token"]
        return token


    def createOrder(self,playwright: Playwright,user_credentials):
        token = self.get_token(playwright,user_credentials)
        api_request_context= playwright.request.new_context(base_url= "https://rahulshettyacademy.com")
        response = api_request_context.post(url="api/ecom/order/create-order",
                                 data= payload,
                                 headers= {"Authorization": token,
                                           "Content-Type": "application/json"})

        print(response.json())
        response_body= response.json()
        order_id= response_body["orders"][0]
        return order_id

    def get_order_details(self,playwright: Playwright):
        pass
