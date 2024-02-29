from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import parse_obj_as
from sqlalchemy.orm import Session

from app.db.models import User
from app.api.models.pydantic_models import UserLoginSchema, UserLoginResponseSchema, UserRegisterSchema, \
    UserRegisterResponseSchema, UserBooksResponseSchema
from app.db.base import get_session_local

router = APIRouter()


@router.post("/register", response_model=UserRegisterResponseSchema, status_code=status.HTTP_201_CREATED)
async def register(item: UserRegisterSchema, db: Session = Depends(get_session_local)) -> UserRegisterResponseSchema:
    user = User().register(db=db, data=item)
    response = parse_obj_as(UserRegisterResponseSchema, user)
    return response


@router.post("/login", response_model=UserLoginResponseSchema, status_code=status.HTTP_200_OK)
async def login(item: UserLoginSchema, db: Session = Depends(get_session_local)) -> UserLoginResponseSchema:
    user = User().login(db=db, data=item)
    if user:
        response = parse_obj_as(UserLoginResponseSchema, user)
        return response
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")


@router.get("/customers", response_model=List[UserLoginResponseSchema], status_code=status.HTTP_200_OK)
async def get_customers(db: Session = Depends(get_session_local)) -> List[UserLoginResponseSchema]:
    users = User().get_all_customer_users(db=db)
    response = parse_obj_as(List[UserLoginResponseSchema], users)
    return response


@router.get("/{user_id}/books", response_model=List[UserBooksResponseSchema], status_code=status.HTTP_200_OK)
async def get_user_books(user_id: int, db: Session = Depends(get_session_local)) -> List[UserBooksResponseSchema]:
    users = User().get_user_books(db=db, user_id=user_id)
    response = parse_obj_as(List[UserBooksResponseSchema], users)
    return response
