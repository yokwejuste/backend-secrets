import logging
import watchtower
from dotenv import load_dotenv
import os

load_dotenv()

AWS_REGION = os.getenv('AWS_REGION')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

logger = logging.getLogger('cloudwatchLogger')
logger.setLevel(logging.INFO)
handler = watchtower.CloudWatchLogHandler(
    log_group='your-log-group',
    stream_name='your-log-stream',
    region_name=AWS_REGION
)
logger.addHandler(handler)

logger.info('This is an info message sent to AWS CloudWatch')
