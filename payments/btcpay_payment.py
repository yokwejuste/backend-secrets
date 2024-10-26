import requests
import os

from dotenv import load_dotenv

load_dotenv()

BTCPAY_API_KEY = os.getenv('BTCPAY_API_KEY')
BTCPAY_BASE_URL = "https://your-btcpay-server.com"


def create_btcpay_invoice(amount, currency, buyer_email):
    """
    Create an invoice in BTCPay Server.

    Args:
        amount (float): The amount to charge.
        currency (str): Currency (e.g., "USD", "BTC").
        buyer_email (str): Buyer's email.

    Returns:
        dict: BTCPay invoice response.
    """
    headers = {
        "Authorization": f"token {BTCPAY_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "price": amount,
        "currency": currency,
        "buyerEmail": buyer_email
    }

    response = requests.post(f"{BTCPAY_BASE_URL}/api/v1/invoices", json=data, headers=headers)
    return response.json()


# Example usage
if __name__ == "__main__":
    invoice = create_btcpay_invoice(
        0.001,
        "BTC",
        "btc_buyer@example.com",
    )
    print(invoice)
