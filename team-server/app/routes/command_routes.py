from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from ..schemas.command_schema import CommandCreate, CommandRead, CommandUpdate
from ..services.command_service import CommandService
from ..database.database import get_db
from ..enums.command_status import CommandStatus

router = APIRouter(prefix="/commands")


@router.get("/", response_model=list[CommandRead])
def list_commands(db: Session = Depends(get_db)):
    return CommandService.get_all(db)

@router.get("/next", response_model=CommandRead)
def get_next_command(db: Session = Depends(get_db)):
    command = CommandService.get_next(db)
    if not command:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No pending command")
    return command

@router.get("/by-status/{status}", response_model=list[CommandRead])
def get_commands_by_status(status: CommandStatus, db: Session = Depends(get_db)):
    return CommandService.get_by_status(db, status.value)


@router.get("/{command_id}", response_model=CommandRead)
def get_command(command_id: int, db: Session = Depends(get_db)):
    command = CommandService.get_by_id(db, command_id)
    if not command:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Command not found")
    return command


@router.post("/", response_model=CommandRead, status_code=status.HTTP_201_CREATED)
def create_command(command_in: CommandCreate, db: Session = Depends(get_db)):
    return CommandService.create(db, command_in.dict())


@router.put("/{command_id}", response_model=CommandRead)
def update_command(command_id: int, command_in: CommandUpdate, db: Session = Depends(get_db)):
    command = CommandService.get_by_id(db, command_id)
    if not command:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Command not found")
    return CommandService.update(db, command, command_in.dict(exclude_unset=True))


@router.delete("/{command_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_command(command_id: int, db: Session = Depends(get_db)):
    command = CommandService.get_by_id(db, command_id)
    if not command:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Command not found")
    CommandService.delete(db, command)
    return None
