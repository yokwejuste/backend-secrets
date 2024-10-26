import os

import boto3
from dotenv import load_dotenv

load_dotenv()

AWS_REGION = os.getenv('AWS_REGION')

# Initialize CloudWatch client
cloudwatch = boto3.client('cloudwatch', region_name=AWS_REGION)


def put_custom_metric(namespace, metric_name, value):
    response = cloudwatch.put_metric_data(
        Namespace=namespace,
        MetricData=[
            {
                'MetricName': metric_name,
                'Value': value,
                'Unit': 'Count'
            },
        ]
    )
    print(f"Metric sent: {metric_name} - Value: {value}")


# Example usage
put_custom_metric("MyAppNamespace", "UserLogins", 1)
