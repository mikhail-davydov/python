# chromadb уже импортирована
# import chromadb
# from chromadb.utils import embedding_functions

# Документы и метаданные — ОБЯЗАТЕЛЬНО используйте эти
documents = [
    "FastAPI — это современный Python-фреймворк для создания API.",
    "Alembic — это инструмент для управления миграциями базы данных в SQLAlchemy.",
    "Общий ответ."
]

metadatas = [
    {"team": "docs"},
    {"team": "backend"},
    {"team": "all"}
]

query, user_team = input().split(', ')

# Создаём клиент
client = chromadb.Client()

# Создаём embedding-функцию
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# Создаём коллекцию
collection = client.create_collection(name="rag", embedding_function=ef)

# Добавляем документы с метаданными
collection.add(
    ids=[f"doc_{i}" for i in range(len(documents))],
    documents=documents,
    metadatas=metadatas
)

# Выполняем поиск с фильтром по команде
results = collection.query(
    query_texts=[query],
    n_results=1,
    where={"team": user_team}
)

# Если не найдено, ищем в общих документах
if not results['documents'][0]:
    results = collection.query(
        query_texts=[query],
        n_results=1,
        where={"team": "all"}
    )

# Выводим первый результат
print(results['documents'][0][0])