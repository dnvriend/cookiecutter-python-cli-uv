# Observability Stack Reference

Reference configurations for running a local observability stack with {{ cookiecutter.project_name }}.

## Components

| Service | Port | Description |
|---------|------|-------------|
| Grafana Alloy | 4317 (gRPC), 4318 (HTTP), 12345 (UI) | OTLP receiver and forwarder |
| Tempo | 3200 | Distributed tracing backend |
| Prometheus | 9090 | Metrics storage |
| Loki | 3100 | Log aggregation |
| Grafana | 3000 | Visualization |

## Quick Start

```bash
# Start the stack
cd references
docker compose up -d

# Configure your CLI to send telemetry
export OTEL_ENABLED=true
export OTEL_EXPORTER_TYPE=otlp
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
{{ cookiecutter.cli_command }} -v
```

Access Grafana at http://localhost:3000 (admin/admin).

## Data Flow

```
{{ cookiecutter.cli_command }} --telemetry
      │
      │ OTLP (gRPC/HTTP)
      ▼
┌─────────────┐
│ Grafana     │
│ Alloy       │
└──────┬──────┘
       │
       ├─── Traces ──────► Tempo ────► Grafana
       │
       ├─── Metrics ─────► Prometheus ► Grafana
       │
       └─── Logs ────────► Loki ──────► Grafana
```

## Configuration

### CLI Telemetry Options

```bash
# Enable via CLI flag
{{ cookiecutter.cli_command }} --telemetry

# Enable via environment
export OTEL_ENABLED=true

# Configure exporter (console or otlp)
export OTEL_EXPORTER_TYPE=otlp

# Configure OTLP endpoint (default: localhost:4317)
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
```

### File Logging (Alternative)

For direct file logging without OTLP:

```bash
# Log to file instead of stderr
export LOG_FILE=/var/log/{{ cookiecutter.project_slug }}.log
{{ cookiecutter.cli_command }} -v
```

### Environment Variables Reference

| Variable | Default | Description |
|----------|---------|-------------|
| `OTEL_ENABLED` | `false` | Enable OpenTelemetry |
| `OTEL_SERVICE_NAME` | `{{ cookiecutter.project_slug }}` | Service name in telemetry |
| `OTEL_EXPORTER_TYPE` | `console` | Exporter type: `console` or `otlp` |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | `http://localhost:4317` | OTLP collector endpoint |
| `OTEL_EXPORTER_OTLP_INSECURE` | `true` | Use insecure connection |
| `LOG_FILE` | (none) | Path to log file (enables file logging) |
| `LOG_FORMAT` | (default format) | Custom log format string |

## Grafana Dashboards

Datasources are automatically provisioned:

- **Prometheus** - Query metrics with PromQL
- **Tempo** - Search and visualize traces
- **Loki** - Search logs with LogQL

### Example Queries

**Traces (Tempo)**
- Search by service: `{ resource.service.name = "{{ cookiecutter.project_slug }}" }`
- Search by trace ID: `{ traceID = "abc123" }`

**Metrics (Prometheus)**
- Request duration: `histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))`

**Logs (Loki)**
- Service logs: `{service_name="{{ cookiecutter.project_slug }}"}`
- Error logs: `{service_name="{{ cookiecutter.project_slug }}"} |= "ERROR"`

## Customization

### Modify Alloy Pipeline

Edit `alloy/config.alloy` to:
- Add additional receivers (Jaeger, Zipkin)
- Add processors (attributes, filtering)
- Configure additional exporters

### Adjust Retention

- **Tempo**: `compactor.compaction.block_retention` in `tempo/tempo.yml`
- **Prometheus**: `--storage.tsdb.retention.time` flag
- **Loki**: `limits_config.retention_period` in `loki/loki-config.yml`

## Cleanup

```bash
# Stop containers
docker compose down

# Remove data volumes
docker compose down -v
```
