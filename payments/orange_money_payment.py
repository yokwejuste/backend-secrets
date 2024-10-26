import requests
import os
from dotenv import load_dotenv

load_dotenv()

ORANGE_APP_ID = os.getenv('ORANGE_APP_ID')
ORANGE_APP_SECRET = os.getenv('ORANGE_APP_SECRET')

def get_orange_access_token():
    """
    Get an access token from Orange Money API.
    """
    url = "https://api.orange.com/oauth/v3/token"
    headers = {
        "Authorization": f"Basic {ORANGE_APP_ID}:{ORANGE_APP_SECRET}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {"grant_type": "client_credentials"}
    orange_token_response = requests.post(url, headers=headers, data=payload)
    return orange_token_response.json()['access_token']


def orange_money_request_payment(phone_number, amount, order_id, currency="XAF"):
    """
    Request a payment via Orange Money.

    Args:
        phone_number (str): The payer's phone number.
        amount (int): The payment amount.
        order_id (str): A unique identifier for the payment.
        currency (str): The currency code, default is XAF.

    Returns:
        dict: Orange Money payment response.
    """
    access_token = get_orange_access_token()
    api_url = "https://api.orange.com/orange-money-webpay/dev/v1/webpayment"
    headers = {"Authorization": f"Bearer {access_token}"}

    payload = {
        "merchant_key": "your_merchant_key",
        "amount": amount,
        "currency": currency,
        "order_id": order_id,
        "return_url": "https://your-return-url.com",
        "cancel_url": "https://your-cancel-url.com",
        "notif_url": "https://your-notif-url.com",
        "lang": "en",
        "reference": "Test Payment",
        "payer": {"id_type": "MSISDN", "id": phone_number}
    }

    om_request_response = requests.post(api_url, json=payload, headers=headers)
    return om_request_response.json()


# Example usage
if __name__ == "__main__":
    response = orange_money_request_payment(
        'XXXXXXXXXXXXX',
        5000,
        'order12345'
    )
    print(response)
