import psutil
from prometheus_client import Gauge, Histogram

# Метрики Prometheus
LLM_RAM_USAGE = Gauge("llm_ram_usage_bytes", "RAM, выделенная под модель")
LLM_INFERENCE_LATENCY = Histogram("llm_inference_latency_seconds", "Время генерации")


class ResourceMonitor:
    def __init__(self):
        self.process = psutil.Process()
        self.initial_ram = self._get_ram()
        LLM_RAM_USAGE.set(0)

    def _get_ram(self) -> int:
        return self.process.memory_info().rss

    def update_ram_metric(self):
        current_ram = self._get_ram()
        model_ram = max(0, current_ram - self.initial_ram)
        LLM_RAM_USAGE.set(model_ram)