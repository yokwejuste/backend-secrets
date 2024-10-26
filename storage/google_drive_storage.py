import os
from io import BytesIO

from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

load_dotenv()

SERVICE_ACCOUNT_FILE = os.getenv('GOOGLE_DRIVE_SERVICE_ACCOUNT_FILE')

SCOPES = ['https://www.googleapis.com/auth/drive']

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

drive_service = build('drive', 'v3', credentials=credentials)


def upload_file_to_drive(file_path, file_name):
    """
    Upload a file to Google Drive.

    Args:
        file_path (str): Path to the local file.
        file_name (str): Name of the file on Google Drive.

    Returns:
        dict: File metadata response from Google Drive.
    """
    file_metadata = {'name': file_name}
    media = MediaFileUpload(file_path, resumable=True)

    try:
        file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(f"File uploaded successfully. File ID: {file.get('id')}")
        return file
    except Exception as e:
        print(f"Error uploading file: {e}")
        return None


def download_file_from_drive(g_file_id, destination):
    """
    Download a file from Google Drive.

    Args:
        g_file_id (str): ID of the file on Google Drive.
        destination (str): Local path to save the downloaded file.
    """
    try:
        request = drive_service.files().get_media(fileId=g_file_id)
        fh = BytesIO()
        downloader = MediaIoBaseDownload(fh, request)

        done = False
        while not done:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}%.")

        with open(destination, 'wb') as f:
            f.write(fh.getvalue())
        print(f"File downloaded successfully to {destination}")
    except Exception as e:
        print(f"Error downloading file: {e}")


def delete_file_from_drive(g_file_id):
    """
    Delete a file from Google Drive.

    Args:
        g_file_id (str): ID of the file on Google Drive.
    """
    try:
        drive_service.files().delete(fileId=g_file_id).execute()
        print(f"File with ID {g_file_id} deleted successfully.")
    except Exception as e:
        print(f"Error deleting file: {e}")


if __name__ == "__main__":
    uploaded_file = upload_file_to_drive("/path/to/file.txt", "uploaded_file.txt")
    if uploaded_file:
        file_id = uploaded_file.get('id')
        download_file_from_drive(file_id, "/path/to/downloaded_file.txt")
        delete_file_from_drive(file_id)
