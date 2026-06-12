from sqlalchemy.orm import Session
from ..models.command import Command


class CommandService:
    @staticmethod
    def get_all(db: Session):
        return db.query(Command).order_by(Command.order).all()

    @staticmethod
    def get_by_id(db: Session, command_id: int):
        return db.query(Command).filter(Command.id == command_id).first()

    @staticmethod
    def create(db: Session, data: dict):
        command = Command(**data)
        db.add(command)
        db.commit()
        db.refresh(command)
        return command

    @staticmethod
    def update(db: Session, command: Command, data: dict):
        for key, value in data.items():
            setattr(command, key, value)
        db.commit()
        db.refresh(command)
        return command

    @staticmethod
    def delete(db: Session, command: Command):
        db.delete(command)
        db.commit()

    @staticmethod
    def get_by_status(db: Session, status: str):
        return db.query(Command).filter(Command.status == status).all()
