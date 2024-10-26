import os

import requests
from dotenv import load_dotenv

load_dotenv()

LAGO_API_KEY = os.getenv('LAGO_API_KEY')
LAGO_BASE_URL = "https://api.getlago.com"


def create_customer(customer_id, email, name):
    """
    Create a customer in GetLago.

    Args:
        customer_id (str): The unique ID for the customer.
        email (str): Customer's email.
        name (str): Customer's name.

    Returns:
        dict: GetLago customer response.
    """
    headers = {
        "Authorization": f"Bearer {LAGO_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "customer": {
            "external_id": customer_id,
            "email": email,
            "name": name
        }
    }

    response = requests.post(f"{LAGO_BASE_URL}/v1/customers", json=data, headers=headers)
    return response.json()


# Example usage
if __name__ == "__main__":
    customer = create_customer(
        "cust_1234",
        "customer@example.com",
        "John Doe",
    )
    print(customer)
