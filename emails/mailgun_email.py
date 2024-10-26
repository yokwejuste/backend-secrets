import os

import requests
from dotenv import load_dotenv

load_dotenv()

MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY')
MAILGUN_DOMAIN = os.getenv('MAILGUN_DOMAIN')


def send_mailgun_email(to_email, subject, message_body, file_path=None):
    """
    Sends an email with an attachment using Mailgun.

    Args:
        to_email (str): Recipient's email address.
        subject (str): Email subject.
        message_body (str): The email message content.
        file_path (str): Optional. The file path to the attachment.

    Returns:
        dict: Response from Mailgun API.
    """
    with open(file_path, 'rb') as attachment:
        return requests.post(
            f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
            auth=("api", MAILGUN_API_KEY),
            files=[("attachment", attachment)],
            data={
                "from": "Your Name <mailgun@your_domain.com>",
                "to": to_email,
                "subject": subject,
                "html": message_body
            }
        )


# Example usage
if __name__ == "__main__":
    response = send_mailgun_email('recipient@example.com', 'Test Email with Attachment from Mailgun',
                                  '<strong>Hello from Mailgun!</strong>', '/tmp/my-file.xlsx')
    print(response.text)
