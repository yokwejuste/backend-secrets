import os

import requests
from dotenv import load_dotenv

load_dotenv()

GA_TRACKING_ID = os.getenv('GA_TRACKING_ID')
GA_API_ENDPOINT = "https://www.google-analytics.com/collect"


def send_event(category, action, label=None, value=None):
    payload = {
        'v': '1',
        'tid': GA_TRACKING_ID,
        'cid': '555',
        't': 'event',
        'ec': category,
        'ea': action,
        'el': label,  # (optional)
        'ev': value,  # (optional)
    }
    response = requests.post(GA_API_ENDPOINT, data=payload)
    print(f"Event sent. Status code: {response.status_code}")


# Example usage
send_event("test_category", "test_action", "test_label", 10)
