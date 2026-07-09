from .auth import router as auth_router
from .me import router as me_router
from .uploads import router as uploads_router

__all__ = ["auth_router", "me_router", "uploads_router"]
