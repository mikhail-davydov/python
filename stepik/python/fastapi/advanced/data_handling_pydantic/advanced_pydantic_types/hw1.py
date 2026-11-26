from pydantic import BaseModel, HttpUrl


class Website(BaseModel):
    title: str
    url: HttpUrl
    backup_url: HttpUrl | None = None
