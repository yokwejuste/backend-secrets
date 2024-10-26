import os
import re

import boto3
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

s3 = boto3.client(
    's3',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)


def upload_file_to_s3(file_path, object_name):
    """
    Uploads a file to S3.

    Args:
        file_path (str): Path to the file to upload.
        object_name (str): S3 object name.
    """
    try:
        s3.upload_file(file_path, AWS_BUCKET_NAME, object_name)
        print(f"File uploaded successfully to {object_name}")
    except Exception as e:
        print(f"Error uploading file: {e}")


def download_file_from_s3(object_name, file_path):
    """
    Downloads a file from S3.

    Args:
        object_name (str): S3 object name.
        file_path (str): Local path to save the file.
    """
    try:
        s3.download_file(AWS_BUCKET_NAME, object_name, file_path)
        print(f"File downloaded successfully to {file_path}")
    except Exception as e:
        print(f"Error downloading file: {e}")


def delete_file_from_s3(file_url):
    """
    Deletes a file from S3 using the provided S3 URL.

    Args:
        file_url (str): The full S3 URL of the file to delete.
    """
    try:
        match = re.match(r"https://(.*)\.s3\.amazonaws\.com/(.*)", file_url)
        if match:
            bucket_name = match.group(1)
            object_key = match.group(2)
        else:
            raise ValueError("Invalid S3 URL format")
        s3.delete_object(Bucket=bucket_name, Key=object_key)
        print(f"File {object_key} from bucket {bucket_name} deleted successfully")

    except Exception as e:
        print(f"Error deleting file: {e}")


# Example usage
if __name__ == "__main__":
    upload_file_to_s3("/path/to/file.txt", "uploaded_file.txt")
    download_file_from_s3("uploaded_file.txt", "/path/to/downloaded_file.txt")
    delete_file_from_s3("https://your-bucket.s3.amazonaws.com/uploaded_file.txt")
