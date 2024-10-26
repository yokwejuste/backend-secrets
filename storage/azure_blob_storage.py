import os
from urllib.parse import urlparse

from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

load_dotenv()

AZURE_CONNECTION_STRING = os.getenv('AZURE_CONNECTION_STRING')
AZURE_CONTAINER_NAME = os.getenv('AZURE_CONTAINER_NAME')

blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)


# Upload a file
def upload_file_to_azure(file_path, blob_name):
    """
    Uploads a file to Azure Blob Storage.

    Args:
        file_path (str): Path to the file to upload.
        blob_name (str): Name of the blob (object).
    """
    blob_client = blob_service_client.get_blob_client(container=AZURE_CONTAINER_NAME, blob=blob_name)

    try:
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data)
        print(f"File {file_path} uploaded successfully to {blob_name}")
    except Exception as e:
        print(f"Error uploading file: {e}")


# Download a file
def download_file_from_azure(blob_name, file_path):
    """
    Downloads a file from Azure Blob Storage.

    Args:
        blob_name (str): Name of the blob (object).
        file_path (str): Path to save the downloaded file.
    """
    blob_client = blob_service_client.get_blob_client(container=AZURE_CONTAINER_NAME, blob=blob_name)

    try:
        with open(file_path, "wb") as file:
            file.write(blob_client.download_blob().readall())
        print(f"File {blob_name} downloaded successfully to {file_path}")
    except Exception as e:
        print(f"Error downloading file: {e}")


def delete_file_from_azure(blob_url):
    """
    Deletes a file from Azure Blob Storage using the blob's URL.

    Args:
        blob_url (str): URL of the blob to delete.
    """
    try:
        parsed_url = urlparse(blob_url)
        blob_name = parsed_url.path.lstrip(f'/{AZURE_CONTAINER_NAME}/')

        blob_client = blob_service_client.get_blob_client(container=AZURE_CONTAINER_NAME, blob=blob_name)

        blob_client.delete_blob()
        print(f"Blob {blob_name} deleted successfully")
    except Exception as e:
        print(f"Error deleting blob: {e}")


if __name__ == "__main__":
    upload_file_to_azure("/path/to/file.txt", "folder1/folder2/uploaded_file.txt")
    download_file_from_azure("folder1/folder2/uploaded_file.txt", "/path/to/downloaded_file.txt")
    delete_file_from_azure("https://youraccount.blob.core.windows.net/yourcontainer/folder1/folder2/uploaded_file.txt")
