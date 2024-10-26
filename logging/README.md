# Logging

This folder contains Python implementations for various logging solutions, including integrations with popular cloud logging services and structured logging setups. Each script provides methods for logging application events, errors, and structured data.

## Contents

- [AWS CloudWatch Logging](#aws-cloudwatch-logging)
- [Azure Monitor Logging](#azure-monitor-logging)
- [Basic Logging](#basic-logging)
- [Google Cloud Logging](#google-cloud-logging)
- [Structured Logging](#structured-logging)

---

### AWS CloudWatch Logging

**AWS CloudWatch Logging** allows you to monitor, store, and access log files from Amazon services, including custom application logs.

- **File**: `aws_cloudwatch_logging.py`
- **Setup**:
  1. Install AWS SDK: `pip install boto3`.
  2. Configure AWS credentials with access to CloudWatch Logs.

- **Example Usage**:
  ```python
  from aws_cloudwatch_logging import setup_cloudwatch_logger
  logger = setup_cloudwatch_logger()
  logger.info("This is an info message sent to AWS CloudWatch.")
  ```

---

### Azure Monitor Logging

**Azure Monitor Logging** enables you to collect and analyze logs from applications and services on Azure. This is part of the broader Azure Monitor suite.

- **File**: `azure_monitor_logging.py`
- **Setup**:
  1. Install Azure SDK: `pip install azure-monitor-opentelemetry`.
  2. Set up Azure Monitor with appropriate credentials.

- **Example Usage**:
  ```python
  from azure_monitor_logging import setup_azure_logger
  logger = setup_azure_logger()
  logger.warning("This is a warning message sent to Azure Monitor.")
  ```

---

### Basic Logging

**Basic Logging** demonstrates how to set up logging in Python using the built-in `logging` module. This is useful for local development or simple logging needs.

- **File**: `basic_logging.py`

- **Example Usage**:
  ```python
  from basic_logging import setup_basic_logger
  logger = setup_basic_logger()
  logger.error("This is an error message in the basic logging setup.")
  ```

---

### Google Cloud Logging

**Google Cloud Logging** (formerly Stackdriver) provides a powerful logging service that integrates with other Google Cloud services.

- **File**: `gcp_logging.py`
- **Setup**:
  1. Install Google Cloud logging client: `pip install google-cloud-logging`.
  2. Configure Google Cloud credentials for authentication.

- **Example Usage**:
  ```python
  from gcp_logging import setup_gcp_logger
  logger = setup_gcp_logger()
  logger.debug("This is a debug message sent to Google Cloud Logging.")
  ```

---

### Structured Logging

**Structured Logging** involves logging data in a structured format (e.g., JSON), making it easier to query and analyze in log management tools.

- **File**: `structured_logging.py`
- **Setup**: No additional dependencies required.

- **Example Usage**:
  ```python
  from structured_logging import setup_structured_logger
  logger = setup_structured_logger()
  logger.info("This is a structured log message.", extra={"user": "admin", "action": "login"})
  ```

---

## How to Use

1. Clone the repository and navigate to the `logging` folder.
2. Install any required dependencies as mentioned in each section.
3. Configure credentials for cloud logging services (AWS, Azure, GCP) where applicable.
4. Run the scripts to log messages to the respective logging service.

## Contributing

Contributions are welcome! If you’d like to add more logging solutions or improve existing implementations, please submit a pull request with a detailed description of your changes.
