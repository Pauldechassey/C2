from enum import Enum

class CommandStatus(str, Enum):
    PENDING = "PENDING"
    DONE = "DONE"
    FAILED = "FAILED"