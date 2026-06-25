import hashlib
import secrets
from sqlalchemy import select

from .database.database import SessionLocal
from .models.user import User

_token: str | None = None


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def get_user(username: str) -> User | None:
    with SessionLocal() as db:
        return db.execute(select(User).filter_by(username=username)).scalar_one_or_none()


def create_user(username: str, password: str) -> User:
    with SessionLocal() as db:
        existing = db.execute(select(User).filter_by(username=username)).scalar_one_or_none()
        if existing:
            return existing
        user = User(username=username, password_hash=hash_password(password))
        db.add(user)
        db.commit()
        db.refresh(user)
        return user


def init() -> str:
    global _token
    create_user("root", "root")
    _token = secrets.token_hex(32)
    return _token


def check_password(username: str, password: str) -> bool:
    user = get_user(username)
    if not user:
        return False
    return secrets.compare_digest(user.password_hash, hash_password(password))


def get_token() -> str:
    return _token or ""


def check_token(token: str) -> bool:
    return secrets.compare_digest(token, _token or "")
