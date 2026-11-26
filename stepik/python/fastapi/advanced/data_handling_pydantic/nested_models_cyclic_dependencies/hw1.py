from typing import Optional

from pydantic import BaseModel


class Profile(BaseModel):
    bio: str = ""
    avatar_url: Optional[str] = None


class User(BaseModel):
    name: str
    profile: 'Profile'  # Отложенная ссылка
