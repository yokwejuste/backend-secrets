[Back to Main README](../README.md)

# Storage

This folder contains Python scripts for integrating various cloud storage services, providing functions for uploading, downloading, and managing files across different providers.

## Contents

- [AWS S3 Storage](#aws-s3-storage)
- [Azure Blob Storage](#azure-blob-storage)
- [Google Cloud Storage](#google-cloud-storage)
- [Google Drive Storage](#google-drive-storage)

---

### AWS S3 Storage

**Amazon S3** is a scalable storage service by Amazon Web Services, commonly used for file storage and backups.

- **File**: `aws_s3_storage.py`
- **Setup**:
  1. Install AWS SDK: `pip install boto3`.
  2. Configure AWS credentials with access to S3.

- **Example Usage**:
  ```python
  from aws_s3_storage import upload_file, download_file
  upload_file("local_file.txt", "my-s3-bucket", "s3_file.txt")
  download_file("my-s3-bucket", "s3_file.txt", "downloaded_file.txt")
  ```

---

### Azure Blob Storage

**Azure Blob Storage** is Microsoft's cloud storage solution for storing large amounts of unstructured data.

- **File**: `azure_blob_storage.py`
- **Setup**:
  1. Install Azure SDK: `pip install azure-storage-blob`.
  2. Configure Azure storage account and access keys.

- **Example Usage**:
  ```python
  from azure_blob_storage import upload_blob, download_blob
  upload_blob("local_file.txt", "my-container", "blob_name.txt")
  download_blob("my-container", "blob_name.txt", "downloaded_file.txt")
  ```

---

### Google Cloud Storage

**Google Cloud Storage** is a unified object storage service by Google, suitable for storing large datasets and backups.

- **File**: `gcp_storage.py`
- **Setup**:
  1. Install Google Cloud client: `pip install google-cloud-storage`.
  2. Configure Google Cloud credentials.

- **Example Usage**:
  ```python
  from gcp_storage import upload_file, download_file
  upload_file("local_file.txt", "my-gcs-bucket", "gcs_file.txt")
  download_file("my-gcs-bucket", "gcs_file.txt", "downloaded_file.txt")
  ```

---

### Google Drive Storage

**Google Drive** provides file storage and synchronization service by Google, allowing users to store and share files.

- **File**: `google_drive_storage.py`
- **Setup**:
  1. Install Google Drive client: `pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client`.
  2. Configure OAuth credentials for Google Drive API.

- **Example Usage**:
  ```python
  from google_drive_storage import upload_to_drive, download_from_drive
  upload_to_drive("local_file.txt", "Drive Folder ID")
  download_from_drive("Drive File ID", "downloaded_file.txt")
  ```

---

## How to Use

1. Clone the repository and navigate to the `storage` folder.
2. Install any required dependencies as mentioned in each section.
3. Configure your credentials for each storage provider.
4. Run the scripts to upload or download files using the specified storage service.

## Contributing

Contributions are welcome! If you’d like to add more storage providers or enhance existing implementations, please submit a pull request with a detailed description of your changes.
