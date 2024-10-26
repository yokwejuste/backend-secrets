import os

import chargebee
from dotenv import load_dotenv

load_dotenv()

CHARGEBEE_SITE = os.getenv('CHARGEBEE_SITE')  # Here you puy your Chargebee site identifier
CHARGEBEE_API_KEY = os.getenv('CHARGEBEE_API_KEY')

chargebee.configure(CHARGEBEE_API_KEY, CHARGEBEE_SITE)


def create_chargebee_subscription(customer_id, plan_id):
    """
    Create a subscription in Chargebee for a customer.

    Args:
        customer_id (str): The unique customer ID.
        plan_id (str): The ID of the plan to subscribe the customer to.

    Returns:
        dict: Chargebee subscription response.
    """
    try:
        result = chargebee.Subscription.create({
            "plan_id": plan_id,
            "customer": {
                "id": customer_id
            }
        })
        print(f"Subscription created successfully: {result['subscription']['id']}")
        return result
    except chargebee.APIError as e:
        print(f"Error creating subscription: {e}")
        return None


# Example usage (create a new subscription)
if __name__ == "__main__":
    subscription = create_chargebee_subscription("customer_12345", "premium_plan")
    print(subscription)


def create_chargebee_customer(email, first_name, last_name):
    """
    Create a new customer in Chargebee.

    Args:
        email (str): The customer's email address.
        first_name (str): Customer's first name.
        last_name (str): Customer's last name.

    Returns:
        dict: Chargebee customer response.
    """
    try:
        result = chargebee.Customer.create({
            "email": email,
            "first_name": first_name,
            "last_name": last_name
        })
        print(f"Customer created successfully: {result['customer']['id']}")
        return result
    except chargebee.APIError as e:
        print(f"Error creating customer: {e}")
        return None


# Example usage (create a new customer)
if __name__ == "__main__":
    customer = create_chargebee_customer("customer@example.com", "John", "Doe")
    print(customer)


def cancel_chargebee_subscription(subscription_id):
    """
    Cancel a subscription in Chargebee.

    Args:
        subscription_id (str): The ID of the subscription to cancel.

    Returns:
        dict: Chargebee subscription cancellation response.
    """
    try:
        result = chargebee.Subscription.cancel(subscription_id, {
            "end_of_term": True
        })
        print(f"Subscription canceled: {result['subscription']['id']}")
        return result
    except chargebee.APIError as e:
        print(f"Error canceling subscription: {e}")
        return None


# Example usage (cancel a subscription)
if __name__ == "__main__":
    cancellation = cancel_chargebee_subscription("sub_12345")
    print(cancellation)
