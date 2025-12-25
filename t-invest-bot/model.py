from dataclasses import dataclass
from typing import Optional


@dataclass
class TokenData:
    """ Класс для хранения токенов """
    read: Optional[str]
    full: Optional[str]
    transfer: Optional[str]
    sandbox: Optional[str]


@dataclass
class UrlData:
    """ Класс для хранения ссылок на env """
    live: Optional[str]
    sandbox: Optional[str]


@dataclass
class Settings:
    """ Главный класс конфигурации """
    account_id: Optional[str]
    token: TokenData
    sandbox_mode: bool
    url: UrlData
