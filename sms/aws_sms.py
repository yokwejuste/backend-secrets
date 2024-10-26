import os

import boto3
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION')


def send_aws_sns_sms(to_phone_number, message_body):
    """
    Sends an SMS message using AWS SNS.

    Args:
        to_phone_number (str): Recipient's phone number.
        message_body (str): The SMS message to be sent.

    Returns:
        dict: Response from AWS SNS with status and message details.
    """
    sms_response = None
    sns_client = boto3.client(
        "sns",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )

    try:
        sms_response = sns_client.publish(
            PhoneNumber=to_phone_number,
            Message=message_body
        )
        print(f"Message sent successfully: {sms_response}")
    except Exception as e:
        print(f"Failed to send message: {str(e)}")

    return sms_response

if __name__ == "__main__":
    send_aws_sns_sms('+XXXXXXXXXX', 'Hello from AWS SNS!')
