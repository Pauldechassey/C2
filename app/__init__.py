from fastapi import FastAPI
from .routes.user_routes import router as user_router
from .database import engine

app = FastAPI(title="User API")
app.include_router(user_router, prefix="/api/users", tags=["users"])


@app.on_event("startup")
def on_startup():
    from .database import Base
    Base.metadata.create_all(bind=engine)
