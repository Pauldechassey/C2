import secrets
import string

_password: str | None = None
_token: str | None = None


def init() -> str:
    global _password, _token
    alphabet = string.ascii_letters + string.digits
    _password = ''.join(secrets.choice(alphabet) for _ in range(16))
    _token = secrets.token_hex(32)
    return _password


def check_password(password: str) -> bool:
    return secrets.compare_digest(password, _password or "")


def get_token() -> str:
    return _token or ""


def check_token(token: str) -> bool:
    return secrets.compare_digest(token, _token or "")
