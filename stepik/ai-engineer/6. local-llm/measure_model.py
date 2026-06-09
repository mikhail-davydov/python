import os
import time
import psutil
from llama_cpp import Llama


def measure_model(model_path: str, prompt: str, n_gen: int = 128):
    current_process = psutil.Process(os.getpid())

    # RAM до загрузки
    ram_before = current_process.memory_info().rss / (1024 ** 3)  # ГБ

    start_load = time.time()
    llm = Llama(
        model_path=model_path,
        n_ctx=2048,
        n_threads=4,
        verbose=False
    )
    load_time = time.time() - start_load
    ram_after = current_process.memory_info().rss / (1024 ** 3)

    start_gen = time.time()
    output = llm(prompt, max_tokens=n_gen, echo=False)
    gen_time = time.time() - start_gen

    return {
        "ram_usage_gb": round(ram_after - ram_before, 2),
        "load_time_s": round(load_time, 2),
        "latency_s": round(gen_time, 2),
        "tokens_per_sec": round(n_gen / gen_time, 1)
    }