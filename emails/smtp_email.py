import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"  # This can be changed to any other SMTP server Office 365, yahoo, etc.)
SMTP_PORT = 587  # This can be changed to the appropriate port for the SMTP server
SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')


def send_smtp_email(to_email, subject, message_body, file_path=None):
    """
    Sends an email with an attachment using an SMTP server (e.g., Gmail).

    Args:
        to_email (str): Recipient's email address.
        subject (str): Email subject.
        message_body (str): The email message content.
        file_path (str): The file path to the attachment.

    Returns:
        None
    """
    msg = MIMEMultipart()
    msg['From'] = SMTP_USER
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message_body, 'html'))

    with open(file_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {os.path.basename(file_path)}')
        msg.attach(part)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_USER, to_email, msg.as_string())


# Example usage
if __name__ == "__main__":
    send_smtp_email(
        'recipient@example.com',
        'Test Email with Attachment from SMTP',
        '<strong>Hello from SMTP!</strong>',
        '/tmp/my-file.xlsx',
    )
