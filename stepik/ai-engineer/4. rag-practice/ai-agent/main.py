import logging
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from langchain_core.messages import HumanMessage

from agent import app, State
from log import setup_logging

setup_logging()
logger = logging.getLogger("agent")

app_api = FastAPI(title="Agent")


# Временное хранилище состояний по user_id (в продакшене — Redis/DB)
_USER_STATES:  dict[str, State] = {}


class QueryRequest(BaseModel):
    user_id: str
    query: str


@app_api.post("/ask")
async def ask(request: QueryRequest):
    try:
        # Загружаем или создаём состояние для user_id
        if request.user_id in _USER_STATES:
            state = _USER_STATES[request.user_id]
            state["messages"].append(HumanMessage(content=request.query))
        else:
            state = {
                "messages": [HumanMessage(content=request.query)],
                "task_id": None
    }

        logger.info("Обработка запроса", extra={"user_id": request.user_id})
        final_state = app.invoke(state)

        # Сохраняем обновлённое состояние
        _USER_STATES[request.user_id] = final_state

        last_message = final_state["messages"][-1]
        answer = getattr(last_message, "content", str(last_message))
        logger.info("Ответ сгенерирован", extra={"user_id": request.user_id})
        return {"answer": answer}

    except Exception as e:
        logger.error("Ошибка при обработке запроса", extra={"error": str(e)})
        raise HTTPException(status_code=500, detail="Сервис временно недоступен")


@app_api.get("/health")
async def health():
    return {"status": "ok"}