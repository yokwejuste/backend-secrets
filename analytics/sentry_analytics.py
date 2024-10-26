import os

import sentry_sdk
from dotenv import load_dotenv

load_dotenv()

SENTRY_DSN = os.getenv('SENTRY_DSN')
sentry_sdk.init(SENTRY_DSN, traces_sample_rate=1.0)


def log_error():
    try:
        1 / 0  # Example error
    except ZeroDivisionError as e:
        sentry_sdk.capture_exception(e)
        print("Error captured by Sentry.")


# Example usage
log_error()
