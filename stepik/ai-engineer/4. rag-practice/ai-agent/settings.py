from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ollama_model: str = "llama3.1"
    ollama_embedding_model: str = "nomic-embed-text"
    docs_dir: str = "./docs"
    log_level: str = "INFO"

settings = Settings()