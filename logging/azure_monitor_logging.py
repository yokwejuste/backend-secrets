import os
from datetime import datetime

from azure.core.exceptions import HttpResponseError
from azure.identity import DefaultAzureCredential
from azure.monitor.ingestion import LogsIngestionClient
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv('DATA_COLLECTION_ENDPOINT')
rule_id = os.getenv('LOGS_DCR_RULE_ID')
stream_name = os.getenv('LOGS_DCR_STREAM_NAME')

credential = DefaultAzureCredential()
client = LogsIngestionClient(endpoint=endpoint, credential=credential, logging_enable=True)

logs = [
    {"Time": datetime.utcnow().isoformat(), "Level": "INFO", "Message": "Log message sent to Azure Monitor"},
    {"Time": datetime.utcnow().isoformat(), "Level": "ERROR", "Message": "An error log message"}
]

try:
    client.upload(rule_id=rule_id, stream_name=stream_name, logs=logs)
    print("Logs uploaded successfully")
except HttpResponseError as e:
    print(f"Failed to upload logs: {e}")
