from fastapi import APIRouter

from app.api.endpoints import user, book

api_router = APIRouter()

api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(book.router, prefix="/books", tags=["books"])
