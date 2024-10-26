import base64
import os

from azure.communication.email import EmailClient
from dotenv import load_dotenv

load_dotenv()

AZURE_COMMUNICATION_CONNECTION_STRING = os.getenv('AZURE_COMMUNICATION_CONNECTION_STRING')


def send_azure_email(to_email, subject, message_body, file_path=None):
    """
    Sends an email with an attachment using Azure Communication Services.

    Args:
        to_email (str): Recipient's email address.
        subject (str): Email subject.
        message_body (str): The email message content.
        file_path (str): The file path to the attachment.

    Returns:
        dict: Response from Azure Communication Services.
    """
    client = EmailClient.from_connection_string(AZURE_COMMUNICATION_CONNECTION_STRING)

    with open(file_path, 'rb') as f:
        file_content = base64.b64encode(f.read()).decode('utf-8')

    message = {
        "content": {
            "subject": subject,
            "html": message_body
        },
        "recipients": {
            "to": [{"address": to_email, "displayName": "Recipient"}]
        },
        "senderAddress": "your_verified_email@example.com",
        "attachments": [
            {
                "name": os.path.basename(file_path),
                "attachmentType": "application/octet-stream",
                "contentInBase64": file_content
            }
        ]
    }

    poller = client.begin_send(message)

    result = poller.result()
    print(f"Email sent successfully with operation ID: {result['id']}")


# Example usage
if __name__ == "__main__":
    send_azure_email('recipient@example.com', 'Test Email with Attachment from Azure',
                     '<strong>Hello from Azure!</strong>', '/tmp/my-file.xlsx')
