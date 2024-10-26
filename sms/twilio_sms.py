import os

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')


def send_twilio_sms(to_phone_number, message_body):
    """
    Sends an SMS message using the Twilio service.

    Args:
        to_phone_number (str): Recipient's phone number.
        message_body (str): The SMS message to be sent.

    Returns:
        str: Message SID if the message was sent successfully.
    """
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        body=message_body,
        from_=TWILIO_PHONE_NUMBER,
        to=to_phone_number
    )
    return message.sid


if __name__ == "__main__":
    sid = send_twilio_sms('+XXXXXXXXXX', 'Hey, Steve trying to reach you!')
    print(f"Message sent with SID: {sid}")
