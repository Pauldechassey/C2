from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    from app.database.database import Base
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown


app = FastAPI(
    title="Team Server API",
    description="Team Server API for C2 operations",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["root"])
def read_root():
    return {"message": "Team Server API is running"}


# Register routers
from app.routes.command_routes import router as command_router
app.include_router(command_router, tags=["commands"])
