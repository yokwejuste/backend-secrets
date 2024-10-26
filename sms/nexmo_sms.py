import os

import vonage
from dotenv import load_dotenv

load_dotenv()

NEXMO_API_KEY = os.getenv('NEXMO_API_KEY')
NEXMO_API_SECRET = os.getenv('NEXMO_API_SECRET')

client = vonage.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)
sms = vonage.Sms(client)


def send_nexmo_sms(to_phone_number, message_body):
    """
    Sends an SMS message using Nexmo (Vonage) service.

    Args:
        to_phone_number (str): Recipient's phone number.
        message_body (str): The SMS message to be sent.

    Returns:
        dict: Response from Nexmo with status and message details.
    """
    response_data = sms.send_message({
        'from': 'NEXMO',
        'to': to_phone_number,
        'text': message_body
    })

    if response_data["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {response_data['messages'][0]['error-text']}")

    return response_data


if __name__ == "__main__":
    response = send_nexmo_sms('+XXXXXXXXXX', 'Hey, Steve trying to reach you!')
    print(response)
