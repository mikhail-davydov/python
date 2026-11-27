from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, PlainSerializer

DateTimeJson = Annotated[
    datetime,
    PlainSerializer(lambda v: v.isoformat(), return_type=str)
]


class Event(BaseModel):
    created_at: DateTimeJson
