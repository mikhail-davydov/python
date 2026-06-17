import asyncio
import fastapi
import httpx
import logging

# Распечатайте прямых потомков root-логгера
root_logger = logging.getLogger()
for logger in root_logger.getChildren():
    print(logger)