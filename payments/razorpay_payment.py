import os
import uuid
import razorpay
from dotenv import load_dotenv

load_dotenv()

RAZORPAY_KEY_ID = os.getenv('RAZORPAY_KEY_ID')
RAZORPAY_KEY_SECRET = os.getenv('RAZORPAY_KEY_SECRET')

client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))


def create_razorpay_payment(amount, currency):
    """
    Create a payment with Razorpay.

    Args:
        amount (int): Payment amount in the smallest currency unit (e.g., paise for INR).
        currency (str): Currency code (e.g., 'INR').

    Returns:
        dict: Razorpay payment response.
    """
    payment = client.order.create({
        "amount": amount,
        "currency": currency,
        "receipt": str(uuid.uuid4()),
        "payment_capture": "1"
    })

    print(f"Payment order created: {payment['id']}")
    return payment


# Example usage
if __name__ == "__main__":
    order = create_razorpay_payment(
        50000,
        'USD',
    )
    print(order)
