from azure.monitor.query import MetricsQueryClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
import os

AZURE_CLIENT_ID = "AZURE_CLIENT_ID"
AZURE_CLIENT_SECRET = "AZURE_CLIENT_SECRET"
AZURE_TENANT_ID = "AZURE_TENANT_ID"

load_dotenv()

credential = DefaultAzureCredential(
    client_id=os.getenv(AZURE_CLIENT_ID),
    client_secret=os.getenv(AZURE_CLIENT_SECRET),
    tenant_id=os.getenv(AZURE_TENANT_ID)
)

client = MetricsQueryClient(credential)

def query_metrics(azure_resource_id):
    response = client.query(azure_resource_id, metric_names=["UserLogins"], timespan="PT1H")
    for metric in response.metrics:
        print(f"Metric name: {metric.name}")
        for time_series in metric.timeseries:
            for data in time_series.data:
                print(f"Timestamp: {data.timestamp}, Value: {data.total}")

# Example usage
resource_id = "/subscriptions/<your-subscription-id>/resourceGroups/<your-resource-group>/providers/Microsoft.Web/sites/<your-site-name>"
query_metrics(resource_id)
