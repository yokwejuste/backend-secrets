from square.client import Client
import os
import uuid

from dotenv import load_dotenv

load_dotenv()

SQUARE_ACCESS_TOKEN = os.getenv('SQUARE_ACCESS_TOKEN')

client = Client(access_token=SQUARE_ACCESS_TOKEN)

def create_square_payment(amount, currency, source_id, location_id):
    """
    Create a payment with Square.

    Args:
        amount (int): Payment amount in the smallest currency unit (e.g., cents for USD).
        currency (str): Currency code (e.g., 'USD').
        source_id (str): Source token or card.
        location_id (str): Square location ID.

    Returns:
        dict: Square payment response.
    """
    response = client.payments.create_payment({
        "source_id": source_id,
        "amount_money": {"amount": amount, "currency": currency},
        "idempotency_key": str(uuid.uuid4()),
        "location_id": location_id
    })

    if response.is_success():
        print(f"Payment successful! Payment ID: {response.body['payment']['id']}")
        return response.body
    else:
        print(f"Payment failed: {response.errors}")
        return None

# Example usage
if __name__ == "__main__":
    payment = create_square_payment(
        5000,
        'USD',
        'source-id-token',
        'location-id',
    )
    print(payment)
