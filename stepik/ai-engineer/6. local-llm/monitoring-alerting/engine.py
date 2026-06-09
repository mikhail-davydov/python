import asyncio
from llama_cpp import Llama
from functools import partial
from concurrent.futures import ThreadPoolExecutor
from metrics import ResourceMonitor, LLM_INFERENCE_LATENCY


class LocalLlmEngine:
    def __init__(self, model_path: str, n_ctx: int = 2048, n_threads: int = 4):
        self.model_path = model_path
        self.n_ctx = n_ctx
        self.n_threads = n_threads
        self._llm: Llama | None = None
        self._executor = ThreadPoolExecutor(max_workers=1)
        self._monitor = ResourceMonitor()

    async def __aenter__(self):
        # Временный пул ТОЛЬКО для загрузки
        with ThreadPoolExecutor(max_workers=1) as temp_executor:
            loop = asyncio.get_running_loop()
            self._llm = await loop.run_in_executor(
                temp_executor,
                partial(Llama, self.model_path, n_ctx=self.n_ctx, n_threads=self.n_threads, verbose=False)
            )
        self._monitor.update_ram_metric()

        # Теперь создаём основной пул для inference
        self._executor = ThreadPoolExecutor(max_workers=1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._llm is not None:
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(self._executor, self._cleanup_llm)
        if not self._executor._shutdown:
            self._executor.shutdown(wait=True)

    def _cleanup_llm(self):
        # Всё освобождение — в синхронном методе
        if self._llm is not None:
            del self._llm
            self._llm = None

    async def generate(self, prompt: str, max_tokens: int = 128) -> str:
        if self._llm is None:
            raise RuntimeError("Model not loaded")

        start = asyncio.get_running_loop().time()
        loop = asyncio.get_running_loop()
        func = partial(self._llm, prompt, max_tokens=max_tokens, echo=False)

        try:
            result = await loop.run_in_executor(self._executor, func)
            latency = asyncio.get_running_loop().time() - start
            LLM_INFERENCE_LATENCY.observe(latency)
            return result["choices"][0]["text"]
        except Exception as e:
            raise RuntimeError(f"Inference failed: {e}") from e
