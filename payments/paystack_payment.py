import os

import requests
from dotenv import load_dotenv

load_dotenv()

PAYSTACK_SECRET_KEY = os.getenv('PAYSTACK_SECRET_KEY')


def create_paystack_payment(amount, email, reference):
    """
    Create a payment request with Paystack.

    Args:
        amount (int): The payment amount in kobo (for NGN).
        email (str): The customer's email.
        reference (str): Unique transaction reference.

    Returns:
        dict: Paystack payment response.
    """
    headers = {
        "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "email": email,
        "amount": amount,  # In kobo for NGN
        "reference": reference
    }

    response = requests.post("https://api.paystack.co/transaction/initialize", json=data, headers=headers)
    return response.json()


# Example usage
if __name__ == "__main__":
    payment = create_paystack_payment(
        50000,
        "customer@example.com",
        "tx_ref_001",
    )
    print(payment)
