from pydantic import BaseModel, field_validator, ConfigDict
import re


class Ticket(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    id: str
    priority: str
    description: str
    
    @field_validator('id')
    @classmethod
    def validate_id(cls, v: str) -> str:
        if not re.match(r'^SUP-\d{4}$', v):
            raise ValueError('id must be SUP- followed by exactly 4 digits')
        return v
    
    @field_validator('priority')
    @classmethod
    def validate_priority(cls, v: str) -> str:
        if v not in ('low', 'medium', 'high'):
            raise ValueError('priority must be low, medium, or high')
        return v
    
    @field_validator('description')
    @classmethod
    def validate_description(cls, v: str) -> str:
        if not v or len(v) > 100:
            raise ValueError('description must be 1-100 characters')
        return v


class SupportRequest(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    ticket: Ticket
    assignee: str
    
    @field_validator('assignee')
    @classmethod
    def validate_assignee(cls, v: str) -> str:
        if v not in ('backend-team', 'frontend-team', 'security-team'):
            raise ValueError('assignee must be backend-team, frontend-team, or security-team')
        return v
