from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String, DateTime
from ..database.database import Base
from ..enums import CommandStatus


class Command(Base):
    __tablename__ = "commands"

    id = Column(Integer, primary_key=True, index=True)
    command = Column(String(10000), unique=True, nullable=False, index=True)
    output = Column(String(10000), nullable=True)
    order = Column(Integer, nullable=False)
    status = Column(String(20), nullable=False, default=CommandStatus.PENDING.value)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
