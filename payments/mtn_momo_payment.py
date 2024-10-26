import os

import requests
from dotenv import load_dotenv

load_dotenv()

MOMO_API_USER = os.getenv('MOMO_API_USER')
MOMO_API_KEY = os.getenv('MOMO_API_KEY')
MOMO_ENVIRONMENT = os.getenv('MOMO_ENVIRONMENT', 'sandbox')  # or 'live' when in production


def get_momo_access_token():
    """
    Get an access token from MTN MoMo API.
    """
    url = f"https://{MOMO_ENVIRONMENT}.momoapi.mtn.com/collection/token/"
    headers = {"Authorization": f"Basic {MOMO_API_KEY}"}
    momo_token_response = requests.post(url, headers=headers)
    return momo_token_response.json()['access_token']


def momo_request_payment(phone_number, amount, external_id, currency="EUR"):
    """
    Request a payment via MTN MoMo.
    """
    access_token = get_momo_access_token()
    api_url = f"https://{MOMO_ENVIRONMENT}.momoapi.mtn.com/collection/v1_0/requesttopay"
    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {
        "amount": str(amount),
        "currency": currency,
        "externalId": external_id,
        "payer": {
            "partyIdType": "MSISDN",
            "partyId": phone_number
        },
        "payerMessage": "Payment for services",
        "payeeNote": "Service payment"
    }

    payment_response = requests.post(api_url, json=payload, headers=headers)
    return payment_response.json()


# Example usage
if __name__ == "__main__":
    response = momo_request_payment(
        '256712345678',
        1000,
        'ext12345',
    )
    print(response)
