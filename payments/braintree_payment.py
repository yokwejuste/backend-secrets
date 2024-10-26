import os

import braintree
from dotenv import load_dotenv

load_dotenv()

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id=os.getenv('BRAINTREE_MERCHANT_ID'),
        public_key=os.getenv('BRAINTREE_PUBLIC_KEY'),
        private_key=os.getenv('BRAINTREE_PRIVATE_KEY')
    )
)


def create_braintree_payment(amount, payment_method_nonce):
    """
    Create a payment with Braintree.

    Args:
        amount (str): Payment amount.
        payment_method_nonce (str): Nonce from the payment method.

    Returns:
        dict: Braintree payment response.
    """
    result = gateway.transaction.sale({
        "amount": amount,
        "payment_method_nonce": payment_method_nonce,
        "options": {"submit_for_settlement": True}
    })

    if result.is_success:
        print(f"Payment successful! Transaction ID: {result.transaction.id}")
        return result.transaction
    else:
        print(f"Payment failed: {result.message}")
        return None


# Example usage
if __name__ == "__main__":
    transaction = create_braintree_payment('10.00', 'fake-valid-nonce')
    print(transaction)
