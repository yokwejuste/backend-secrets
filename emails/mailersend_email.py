import os

import requests
from dotenv import load_dotenv

load_dotenv()

MAILERSEND_API_KEY = os.getenv('MAILERSEND_API_KEY')


def send_mailersend_email(to_email, subject, message_body, file_path):
    """
    Sends an email with an attachment using MailerSend.

    Args:
        to_email (str): Recipient's email address.
        subject (str): Email subject.
        message_body (str): The email message content.
        file_path (str): The file path to the attachment.

    Returns:
        dict: Response from MailerSend API.
    """
    with open(file_path, 'rb') as f:
        files = {
            'attachments': (os.path.basename(file_path), f, 'application/octet-stream')
        }

        data = {
            "from": {
                "email": "your_verified_email@example.com",
                "name": "Your Name"
            },
            "to": [
                {"email": to_email, "name": "Recipient Name"}
            ],
            "subject": subject,
            "html": message_body
        }

        headers = {
            "Authorization": f"Bearer {MAILERSEND_API_KEY}",
            "Content-Type": "application/json"
        }

        email_response = requests.post(
            "https://api.mailersend.com/v1/email",
            headers=headers,
            json=data,
            files=files
        )

    return email_response.json()


# Example usage
if __name__ == "__main__":
    response = send_mailersend_email('recipient@example.com', 'Test Email with Attachment from MailerSend',
                                     '<strong>Hello from MailerSend!</strong>', '/tmp/my-file.xlsx')
    print(response)
