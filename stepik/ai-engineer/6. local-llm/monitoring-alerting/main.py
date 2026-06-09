from fastapi import FastAPI, Request
from contextlib import asynccontextmanager

from engine import LocalLlmEngine
from health import deep_healthcheck
from recovery import SelfHealingEngine


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with LocalLlmEngine("./mistral-7b-instruct-v0.3-q4_k_m.gguf") as engine:
        app.state.llm = SelfHealingEngine(engine)
        yield


app = FastAPI(lifespan=lifespan)


@app.get("/health")
async def health_check(request: Request):
    healthy = await deep_healthcheck(request.app.state.llm)
    return {"status": "healthy" if healthy else "unhealthy"}


@app.post("/generate")
async def generate(prompt: str, request: Request):
    answer = await request.app.state.llm.generate(prompt)
    return {"answer": answer}
