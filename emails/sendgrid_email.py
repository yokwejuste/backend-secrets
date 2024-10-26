import base64
import os

from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition

load_dotenv()

SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')


def send_sendgrid_email(to_email, subject, message_body, file_path=None):
    """
    Sends an email using Twilio SendGrid, with optional file attachment.

    Args:
        to_email (str): Recipient's email address.
        subject (str): Email subject.
        message_body (str): The email message content.
        file_path (str): Optional path to a file to send as an attachment.

    Returns:
        dict: Response from SendGrid.
    """
    message = Mail(
        from_email='your_verified_email@example.com',
        to_emails=to_email,
        subject=subject,
        html_content=message_body
    )

    if file_path:
        with open(file_path, 'rb') as f:
            file_data = f.read()
            encoded_file = base64.b64encode(file_data).decode('utf-8')

        attachment = Attachment(
            FileContent(encoded_file),
            FileName(os.path.basename(file_path)),
            FileType('application/octet-stream'),
            Disposition('attachment')
        )
        message.attachment = attachment

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"Email sent successfully with status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending email: {str(e)}")


# Example usage
if __name__ == "__main__":
    send_sendgrid_email(
        'recipient@example.com',
        'Test Email with Attachment',
        '<strong>Hello from SendGrid!</strong>',
        '/path/to/file.xlsx',
    )
