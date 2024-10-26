import os

import requests
from requests.auth import HTTPBasicAuth

MPESA_CONSUMER_KEY = os.getenv('MPESA_CONSUMER_KEY')
MPESA_CONSUMER_SECRET = os.getenv('MPESA_CONSUMER_SECRET')
MPESA_SHORTCODE = os.getenv('MPESA_SHORTCODE')
MPESA_PASSKEY = os.getenv('MPESA_PASSKEY')


def get_mpesa_access_token():
    """
    Retrieve the access token from M-Pesa API.
    """
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(url, auth=HTTPBasicAuth(MPESA_CONSUMER_KEY, MPESA_CONSUMER_SECRET))
    access_token = response.json()['access_token']
    return access_token


def mpesa_stk_push(phone_number, amount, account_reference, transaction_desc):
    """
    Perform an STK Push (Sim Tool Kit) payment request using M-Pesa.
    """
    access_token = get_mpesa_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {
        "BusinessShortCode": MPESA_SHORTCODE,
        "Password": "your_password_here",
        "Timestamp": "20240101010101",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": MPESA_SHORTCODE,
        "PhoneNumber": phone_number,
        "CallBackURL": "https://your-callback-url.com",
        "AccountReference": account_reference,
        "TransactionDesc": transaction_desc
    }

    payment_response = requests.post(api_url, json=payload, headers=headers)
    return payment_response.json()


# Example usage
if __name__ == "__main__":
    response = mpesa_stk_push(
        '254712345678',
        1000,
        'TestRef123',
        'Test Payment',
    )
    print(response)
