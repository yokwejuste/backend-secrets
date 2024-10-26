import paypalrestsdk
import os
from dotenv import load_dotenv

load_dotenv()

paypalrestsdk.configure({
    "mode": "sandbox",  # Use "live" for production
    "client_id": os.getenv('PAYPAL_CLIENT_ID'),
    "client_secret": os.getenv('PAYPAL_CLIENT_SECRET')
})

def create_paypal_payment(total, currency, description, return_url, cancel_url):
    """
    Create a PayPal payment.

    Args:
        total (str): Payment amount.
        currency (str): Currency code (e.g., 'USD').
        description (str): Description of the payment.
        return_url (str): URL to redirect after successful payment.
        cancel_url (str): URL to redirect after a failed or canceled payment.

    Returns:
        dict: PayPal payment response.
    """
    paypal_payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {"payment_method": "paypal"},
        "transactions": [{"amount": {"total": total, "currency": currency}, "description": description}],
        "redirect_urls": {"return_url": return_url, "cancel_url": cancel_url}
    })

    if paypal_payment.create():
        print(f"Payment created successfully: {paypal_payment.id}")
        return paypal_payment
    else:
        print(paypal_payment.error)
        return None

# Example usage
if __name__ == "__main__":
    payment = create_paypal_payment(
        '10.00',
        'USD',
        'Test Payment from PayPal',
        'https://your-return-url.com',
        'https://your-cancel-url.com',
    )
    print(payment)
