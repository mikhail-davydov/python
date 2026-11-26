from typing import Literal

from pydantic import BaseModel, Field


class Task(BaseModel):
    title: str
    status: Literal["new", "in_progress", "done"] = "new"
    tags: list[str] = Field(default_factory=list)
