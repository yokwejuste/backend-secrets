import os
from urllib.parse import urlparse

from dotenv import load_dotenv
from google.cloud import storage

load_dotenv()

GOOGLE_CLOUD_PROJECT = os.getenv('GOOGLE_CLOUD_PROJECT')
GCP_BUCKET_NAME = os.getenv('GCP_BUCKET_NAME')


def get_gcp_client():
    return storage.Client()


def upload_file_to_gcs(file_path, blob_name):
    """
    Uploads a file to Google Cloud Storage.

    Args:
        file_path (str): Path to the file to upload.
        blob_name (str): Name of the blob (object).
    """
    client = get_gcp_client()
    bucket = client.bucket(GCP_BUCKET_NAME)
    blob = bucket.blob(blob_name)

    try:
        blob.upload_from_filename(file_path)
        print(f"File {file_path} uploaded successfully to {blob_name}")
    except Exception as e:
        print(f"Error uploading file: {e}")


def download_file_from_gcs(blob_name, file_path):
    """
    Downloads a file from Google Cloud Storage.

    Args:
        blob_name (str): Name of the blob (object).
        file_path (str): Path to save the downloaded file.
    """
    client = get_gcp_client()
    bucket = client.bucket(GCP_BUCKET_NAME)
    blob = bucket.blob(blob_name)

    try:
        blob.download_to_filename(file_path)
        print(f"File {blob_name} downloaded successfully to {file_path}")
    except Exception as e:
        print(f"Error downloading file: {e}")


def delete_file_from_gcs(file_url):
    """
    Deletes a file from Google Cloud Storage given a full URL.

    Args:
        file_url (str): The full URL of the file in GCS.
    """
    client = get_gcp_client()

    try:
        parsed_url = urlparse(file_url)
        bucket_name = parsed_url.netloc
        blob_name = parsed_url.path.lstrip('/')

        bucket = client.bucket(bucket_name)
        blob = bucket.blob(blob_name)

        blob.delete()
        print(f"File {blob_name} deleted successfully from bucket {bucket_name}")
    except Exception as e:
        print(f"Error deleting file: {e}")


if __name__ == "__main__":
    upload_file_to_gcs("/path/to/file.txt", "uploaded_file.txt")
    download_file_from_gcs("uploaded_file.txt", "/path/to/downloaded_file.txt")
    delete_file_from_gcs("https://storage.googleapis.com/your-bucket/uploaded_file.txt")
