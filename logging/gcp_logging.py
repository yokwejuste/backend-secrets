import logging
import os

import google.cloud.logging
from dotenv import load_dotenv
from google.cloud.logging.handlers import CloudLoggingHandler

load_dotenv()

gcp_credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

if not gcp_credentials_path:
    raise EnvironmentError("GOOGLE_APPLICATION_CREDENTIALS environment variable not set")

try:
    client = google.cloud.logging.Client()
except Exception as e:
    logging.error(f"Failed to initialize Google Cloud client: {e}")
    raise

try:
    handler = CloudLoggingHandler(client)
    logger = logging.getLogger('gcpLogger')
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
except Exception as e:
    logging.error(f"Failed to set up Google Cloud Logging handler: {e}")
    raise


def log_message(message, level=logging.INFO):
    try:
        if level == logging.INFO:
            logger.info(message)
        elif level == logging.WARNING:
            logger.warning(message)
        elif level == logging.ERROR:
            logger.error(message)
        elif level == logging.DEBUG:
            logger.debug(message)
        else:
            logger.log(level, message)
        print(f"Log sent to Google Cloud: {message}")
    except Exception as e:
        logging.error(f"Failed to send log to Google Cloud Logging: {e}")
        print(f"Error sending log: {e}")


# Example usage
if __name__ == "__main__":
    log_message("This is an info message sent to Google Cloud Logging", logging.INFO)
    log_message("This is a warning message", logging.WARNING)
    log_message("This is an error message", logging.ERROR)
