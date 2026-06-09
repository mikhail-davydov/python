# AI Agent — RAG-система с инструментами

AI-агент для компании TSI, использующий RAG (Retrieval-Augmented Generation) для ответов на вопросы по внутренней документации и управления задачами.

## Возможности

- **Поиск по документации**: агент отвечает на вопросы, используя внутреннюю документацию компании
- **Управление задачами**: создание задач и добавление комментариев в трекере
- **Stateful-взаимодействие**: поддержка контекста диалога для каждого пользователя
- **JSON-логирование**: структурированное логирование в формате JSON

## Требования

- Python 3.10+
- [Ollama](https://github.com/ollama/ollama) (локальный LLM-сервер)
- Модели Ollama: `llama3.1` и `nomic-embed-text`

## Установка

1. Клонируйте репозиторий и перейдите в директорию проекта:

```bash
cd stepik/ai-engineer/rag-practice/ai-agent
```

2. Создайте виртуальное окружение и установите зависимости:

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/MacOS

pip install -r requirements.txt
```

3. Загрузите необходимые модели Ollama:

```bash
ollama pull llama3.1
ollama pull nomic-embed-text
```

## Конфигурация

Настройки хранятся в [`settings.py`](settings.py):

| Параметр | Описание | По умолчанию |
|----------|----------|--------------|
| `ollama_model` | Модель LLM для генерации ответов | `llama3.1` |
| `ollama_embedding_model` | Модель для эмбеддингов | `nomic-embed-text` |
| `docs_dir` | Директория с документацией | `./docs` |
| `log_level` | Уровень логирования | `INFO` |

Документация для поиска должна находиться в директории `docs/` (файлы `.md`).

## Запуск

```bash
uvicorn main:app_api --reload
```

Сервер запустится по адресу: `http://localhost:8000`

## API Endpoints

### POST /ask

Отправка запроса агенту.

**Request Body:**

```json
{
  "user_id": "string",
  "query": "string"
}
```

**Response:**

```json
{
  "answer": "string"
}
```

### GET /health

Проверка здоровья сервиса.

**Response:**

```json
{
  "status": "ok"
}
```

## Примеры использования

### 1. Информационный запрос (RAG)

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"user_id": "alice", "query": "Что такое RAG и для чего используется?"}'
```

**Ответ:**

```json
{"answer": "Информация по этому запросу в документации найдена. RAG (Retrieval-Augmented Generation) — это система, которая используется для ответов на вопросы по документам."}
```

### 2. Создание задачи

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"user_id": "alice", "query": "Создай задачу: добавить пример агента"}'
```

**Ответ:**

```json
{"answer": "Задача создана с номером TSI-777. В ближайшее время будет добавлен пример агента в документацию."}
```

### 3. Уточнение по задаче (stateful)

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"user_id": "alice", "query": "А теперь добавь комментарий: сделано"}'
```

**Ответ:**

```json
{"answer": "Задача TSI-777 решена. Пример агента добавлен в документацию."}
```

## Структура проекта

```
ai-agent/
├── agent.py          # Логика AI-агента (LangGraph)
├── main.py           # FastAPI-приложение
├── retriever.py      # RAG- retrieval (Chroma + Ollama)
├── tools.py          # Инструменты агента
├── settings.py       # Конфигурация
├── log.py            # Настройка JSON-логирования
├── docs/             # Документация для поиска
├── requirements.txt  # Зависимости
└── README.md         # Этот файл
```

## Архитектура

Агент построен на [LangGraph](https://langchain-ai.github.io/langgraph/) и включает:

1. **Узел `agent`** — вызов LLM с привязкой к инструментам
2. **Узел `tools`** — выполнение инструментов (search_docs, create_task, add_comment)
3. **Узел `update`** — обновление состояния после выполнения инструментов

Граф направляет поток:
```
START → agent → [tools → update] → agent → __end__
```
