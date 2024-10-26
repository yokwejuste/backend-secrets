1. **Docker Compose**: Use Docker Compose to run Prometheus with Python.

   **docker-compose.yml**
   ```yaml
   version: '3.8'
   services:
     prometheus:
       image: prom/prometheus
       container_name: prometheus
       volumes:
         - ./prometheus.yml:/etc/prometheus/prometheus.yml
       ports:
         - "9090:9090"
   ```

2. **Prometheus Configuration**: Define Prometheus scraping intervals and target services.

   **prometheus.yml**
   ```yaml
   global:
     scrape_interval: 15s

   scrape_configs:
     - job_name: 'python_app'
       scrape_interval: 5s
       static_configs:
         - targets: ['host.docker.internal:8000']
   ```

3. **Python Code**: Use the `prometheus_client` library in Python to create and expose metrics.

   **prometheus_example.py**
   ```python
   from prometheus_client import start_http_server, Summary, Counter
   import time
   import random

   REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
   REQUEST_COUNT = Counter('request_count', 'Total number of requests')

   @REQUEST_TIME.time()
   def process_request():
       REQUEST_COUNT.inc()
       time.sleep(random.random())

   if __name__ == '__main__':
       start_http_server(8000)
       while True:
           process_request()
   ```
