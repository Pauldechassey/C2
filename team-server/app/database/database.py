import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, "..", ".env"))

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///./commands.db")

connect_args = {"check_same_thread": False} if SQLALCHEMY_DATABASE_URI.startswith("sqlite") else {}
engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
