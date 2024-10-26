import json
import logging


class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_message = {
            'level': record.levelname,
            'message': record.getMessage(),
            'timestamp': self.formatTime(record, self.datefmt),
            'name': record.name
        }
        return json.dumps(log_message)


logger = logging.getLogger('structuredLogger')
handler = logging.FileHandler('structured_app.log')
formatter = JSONFormatter()
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.info('Structured info message')
logger.error('Structured error message')
