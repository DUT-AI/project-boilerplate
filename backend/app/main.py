from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.infrastructure.di import setup_di
from app.presentation.api.exceptions import setup_exception_handlers
from app.presentation.api.routers import auth_router, me_router, uploads_router

app = FastAPI(
    title="Clean Architecture Boilerplate API",
    description="FastAPI Backend boilerplate with Clean Architecture, DI (Dishka), PostgreSQL, and S3",
    version="1.0.0",
)

# Setup Exception Handlers
setup_exception_handlers(app)

# Setup Dependency Injection
setup_di(app)

# Configure CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API Routers
app.include_router(auth_router, prefix="/api/v1")
app.include_router(me_router, prefix="/api/v1")
app.include_router(uploads_router, prefix="/api/v1")


@app.get("/health", tags=["health"])
async def health_check():
    """Simple health check endpoint."""
    return {"status": "ok", "version": "1.0.0"}
