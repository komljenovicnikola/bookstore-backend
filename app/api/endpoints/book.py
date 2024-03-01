from fastapi import APIRouter, Depends, status
from pydantic import TypeAdapter
from sqlalchemy.orm import Session

from app.db.models import Book
from app.api.models.pydantic_models import BookSchema, BookResponseSchema
from app.db.base import get_session_local

router = APIRouter()


@router.post("/borrow", response_model=BookResponseSchema, status_code=status.HTTP_201_CREATED)
async def borrow(item: BookSchema, db: Session = Depends(get_session_local)) -> BookResponseSchema:
    book_data = Book().create_and_borrow(db=db, data=item)
    ta = TypeAdapter(BookResponseSchema)
    response = ta.validate_python(book_data)
    return response


@router.put("/{book_id}", response_model=BookResponseSchema, status_code=status.HTTP_200_OK)
async def update_book(book_id: int, item: BookSchema, db: Session = Depends(get_session_local)) -> BookResponseSchema:
    book_data = Book().update_book(db=db, book_id=book_id, data=item)
    ta = TypeAdapter(BookResponseSchema)
    response = ta.validate_python(book_data)
    return response


@router.delete("/{user_id}/return/{book_id}", response_model=BookResponseSchema, status_code=status.HTTP_200_OK)
async def return_book(user_id: int, book_id: int, db: Session = Depends(get_session_local)) -> BookResponseSchema:
    response = Book().return_book(db=db, book_id=book_id, user_id=user_id)
    ta = TypeAdapter(BookResponseSchema)
    response = ta.validate_python(response)
    return response
