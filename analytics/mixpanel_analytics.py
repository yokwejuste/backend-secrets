import os

from dotenv import load_dotenv
from mixpanel import Mixpanel

load_dotenv()

MIXPANEL_PROJECT_TOKEN = os.getenv('MIXPANEL_PROJECT_TOKEN')
mp = Mixpanel(MIXPANEL_PROJECT_TOKEN)


def track_event(event_name, distinct_id, properties=None):
    mp.track(distinct_id, event_name, properties)
    print(f"Event '{event_name}' tracked for user {distinct_id}")


# Example usage
track_event("UserSignUp", "user_123", {"plan": "premium"})
