import os

import africastalking
from dotenv import load_dotenv

load_dotenv()

AT_API_KEY = os.getenv('AT_API_KEY')
AT_USERNAME = os.getenv('AT_USERNAME')

africastalking.initialize(AT_USERNAME, AT_API_KEY)
sms = africastalking.SMS


def send_africastalking_sms(to_phone_number, message_body):
    """
    Sends an SMS message using Africa's Talking service.

    Args:
        to_phone_number (str): Recipient's phone number.
        message_body (str): The SMS message to be sent.

    Returns:
        dict: Response from Africa's Talking with status and message details.
    """
    sms_response = None
    try:
        sms_response = sms.send(message_body, [to_phone_number])
        print(f"Message sent successfully: {sms_response}")
    except Exception as e:
        print(f"Failed to send message: {str(e)}")
    return sms_response


if __name__ == "__main__":
    response = send_africastalking_sms('+XXXXXXXXXXX', 'Hello from Africa\'s Talking!')
    print(response)
