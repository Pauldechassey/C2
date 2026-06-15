import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedir, "..", ".env"))


class Config:
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///./app.db"
    )
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
