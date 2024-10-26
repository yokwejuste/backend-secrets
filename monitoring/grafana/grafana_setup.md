1. **Docker Compose**: Use Docker Compose to run Grafana along with Prometheus.

   Add Grafana service to **docker-compose.yml**
   ```yaml
   grafana:
     image: grafana/grafana
     container_name: grafana
     ports:
       - "3000:3000"
     environment:
       - GF_SECURITY_ADMIN_PASSWORD=admin
   ```

2. **Grafana Setup**: After starting the Docker Compose setup, log in to Grafana at `http://localhost:3000` with default credentials (`admin/admin`).
3. **Add Data Source**:
   - Go to **Configuration > Data Sources** in Grafana.
   - Add Prometheus with the URL `http://prometheus:9090`.

#### Process
1. Create dashboards in Grafana using the imported Prometheus metrics.
2. Set up alerts on critical metrics (e.g., request time or count).
