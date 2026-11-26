from datetime import datetime
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

# Создайте модель Event.
class Event(BaseModel):
    name: str
    event_id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.now)
    metadata: dict[str, str] = Field(default_factory=dict)