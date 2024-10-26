1. **Docker Compose**: Run Datadog Agent in Docker and configure it to monitor the Python app.

   **docker-compose.yml**
   ```yaml
   datadog:
     image: datadog/agent:latest
     environment:
       - DD_API_KEY=your_datadog_api_key
       - DD_LOGS_ENABLED=true
       - DD_APM_ENABLED=true
     volumes:
       - /var/run/docker.sock:/var/run/docker.sock
       - /proc/:/host/proc/:ro
       - /sys/fs/cgroup:/host/sys/fs/cgroup:ro
   ```

2. **Python Code**: Use `ddtrace` library for tracing requests.

   ```bash
   pip install ddtrace
   ```

   **datadog_example.py**
   ```python
   from ddtrace import tracer

   @tracer.wrap(name="custom_request_trace")
   def process_request():
       time.sleep(random.random())
   ```
   