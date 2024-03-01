from pydantic import BaseModel


class BaseConfig(BaseModel):
    class Config:
        from_attributes = True


class UserLoginSchema(BaseConfig):
    email: str
    password: str


class UserResponseSchema(BaseConfig):
    id: int
    email: str
    first_name: str
    last_name: str
    role: str


class UserRegisterSchema(BaseConfig):
    email: str
    first_name: str
    last_name: str
    password: str


class BookSchema(BaseConfig):
    title: str
    author: str
    year: int
    user_id: int


class BookResponseSchema(BaseConfig):
    id: int
    title: str
    author: str
    year: int
