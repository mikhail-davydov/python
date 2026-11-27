from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, WrapSerializer


def wrap_datetime(value: datetime, handler):
    result = handler(value)
    return f"[{result}]"


DateTimeWrapped = Annotated[
    datetime,
    WrapSerializer(wrap_datetime, return_type=str)
]


class LogEntry(BaseModel):
    timestamp: DateTimeWrapped
