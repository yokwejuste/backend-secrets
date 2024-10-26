import stripe
import os

STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

def create_stripe_payment(amount, currency, source, description):
    """
    Create a payment with Stripe.

    Args:
        amount (int): Amount to charge (in the smallest unit of the currency, e.g., cents for USD).
        currency (str): Currency code (e.g., 'usd').
        source (str): Source token or card.
        description (str): Description of the payment.

    Returns:
        dict: Stripe payment response.
    """
    try:
        stripe_charge = stripe.Charge.create(
            amount=amount,
            currency=currency,
            source=source,
            description=description
        )
        print(f"Payment successful! Charge ID: {stripe_charge.id}")
        return stripe_charge
    except stripe.error.StripeError as e:
        print(f"Payment failed: {e.error.message}")
        return None

# Example usage
if __name__ == "__main__":
    charge = create_stripe_payment(
        5000,
        'usd',
        'tok_visa',
        'Test Payment from Stripe',
    )
    print(charge)
