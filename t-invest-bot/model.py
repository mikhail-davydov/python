from dataclasses import dataclass
from typing import Optional


@dataclass
class TokenData:
    """Класс для хранения токенов"""
    read: Optional[str]
    full: Optional[str]
    transfer: Optional[str]
    sandbox: Optional[str]


@dataclass
class Settings:
    """Главный класс конфигурации"""
    token: TokenData
    sandbox_mode: bool
