from prometheus_client import start_http_server, Gauge
import random, time

cpu_usage = Gauge("cpu_usage", "CPU usage in percent")

def monitor_cpu():
    while True:
        usage = random.uniform(10, 90)
        cpu_usage.set(usage)
        time.sleep(2)

start_http_server(8000)
monitor_cpu()
