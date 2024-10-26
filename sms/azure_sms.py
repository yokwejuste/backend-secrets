import os

from azure.communication.sms import SmsClient
from dotenv import load_dotenv

load_dotenv()

AZURE_COMMUNICATION_CONNECTION_STRING = os.getenv('AZURE_COMMUNICATION_CONNECTION_STRING')


def send_azure_sms(to_phone_number, message_body):
    """
    Sends an SMS message using Azure Communication Services.

    Args:
        to_phone_number (str): Recipient's phone number.
        message_body (str): The SMS message to be sent.

    Returns:
        str: The response from Azure Communication Services.
    """
    sms_client = SmsClient.from_connection_string(AZURE_COMMUNICATION_CONNECTION_STRING)

    try:
        response = sms_client.send(
            from_='<Your Azure Phone Number>',
            to=[to_phone_number],
            message=message_body,
            enable_delivery_report=True
        )
        print("Message sent successfully:", response)
    except Exception as e:
        print(f"Failed to send message: {str(e)}")


# Example usage
if __name__ == "__main__":
    send_azure_sms('+XXXXXXXXXXX', 'Hello from Azure Communication Services!')
