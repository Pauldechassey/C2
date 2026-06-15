import logging
import time
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import engine

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger("team-server")


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

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = (time.time() - start) * 1000
    client = request.client.host if request.client else "unknown"
    logger.info(f"{client} | {request.method} {request.url.path} | {response.status_code} | {duration:.1f}ms")
    return response

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
