from pydantic import BaseModel


class UserLoginSchema(BaseModel):
    email: str
    password: str

    class Config:
        from_attributes = True
        model = 'User'


class UserLoginResponseSchema(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    role: str

    class Config:
        from_attributes = True
        model = 'User'


class UserRegisterSchema(BaseModel):
    email: str
    first_name: str
    last_name: str
    password: str

    class Config:
        from_attributes = True
        model = 'User'


class UserRegisterResponseSchema(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    role: str

    class Config:
        from_attributes = True
        model = 'User'


class UserBooksResponseSchema(BaseModel):
    id: int
    title: str
    author: str
    year: int

    class Config:
        from_attributes = True
        model = 'Book'


class BookSchema(BaseModel):
    title: str
    author: str
    year: int
    user_id: int

    class Config:
        from_attributes = True
        model = 'Book'


class BookResponseSchema(BaseModel):
    id: int
    title: str
    author: str
    year: int

    class Config:
        from_attributes = True
        model = 'Book'

