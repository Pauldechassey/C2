from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.enums.command_status import CommandStatus


class CommandBase(BaseModel):
    command: str = Field(..., min_length=1, max_length=10000)
    order: int
    status: CommandStatus = CommandStatus.PENDING
    output: Optional[str] = None


class CommandCreate(CommandBase):
    pass


class CommandUpdate(BaseModel):
    command: Optional[str] = Field(None, min_length=1, max_length=10000)
    order: Optional[int] = None
    status: Optional[CommandStatus] = None
    output: Optional[str] = None


class CommandRead(CommandBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
