import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import boto3

AWS_REGION = os.getenv('AWS_REGION')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')


def send_aws_ses_email(to_email, subject, message_body, file_path=None):
    """
    Sends an email with an attachment using AWS SES.

    Args:
        to_email (str): Recipient's email address.
        subject (str): Email subject.
        message_body (str): The email message content.
        file_path (str): Optional. Path to the file to be attached.

    Returns:
        dict: Response from AWS SES.
    """
    client = boto3.client(
        'ses',
        region_name=AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )

    msg = MIMEMultipart()
    msg['From'] = 'a_verified_email@example.com'
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message_body, 'html'))

    with open(file_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {os.path.basename(file_path)}')
        msg.attach(part)

    try:
        response = client.send_raw_email(
            Source=msg['From'],
            Destinations=[to_email],
            RawMessage={'Data': msg.as_string()}
        )
        print(f"Email sent successfully! Message ID: {response['MessageId']}")
    except Exception as e:
        print(f"Error sending email: {str(e)}")


# Example usage
if __name__ == "__main__":
    send_aws_ses_email(
        'recipient@example.com',
        'Test Email with Attachment from SES',
        '<strong>Hello from AWS SES!</strong>',
        '/tmp/my-file.xlsx',
    )
