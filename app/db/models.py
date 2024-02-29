import enum

from passlib.hash import bcrypt
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.db.base import Base

user_books = Table(
    'user_books',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('book_id', Integer, ForeignKey('books.id'), primary_key=True)
)


class UserRole(enum.Enum):
    customer = "customer"
    admin = "admin"
    librarian = "librarian"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String, unique=False)
    last_name = Column(String, unique=False)
    _password = Column('password', String)
    role = Column(Enum(UserRole, name="user_role_enum"), default=UserRole.customer)
    books = relationship("Book", secondary=user_books, backref="borrowers")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = bcrypt.hash(password)

    def verify_password(self, password):
        return bcrypt.verify(password, self._password)

    @classmethod
    def login(cls, db, data):
        user = db.query(User).filter(User.email == data.email).first()
        if user and user.verify_password(data.password):
            return user
        return None

    @classmethod
    def register(cls, db, data):
        user = User(**data.dict())
        user.password = data.password
        db.add(user)
        db.commit()
        return user

    @classmethod
    def get_all_customer_users(cls, db):
        return db.query(User).filter(User.role == UserRole.customer).all()

    @classmethod
    def get_user_books(cls, db, user_id):
        return db.query(User).filter(User.id == user_id).first().books


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=False)
    author = Column(String, unique=False)
    year = Column(Integer, unique=False)

    @classmethod
    def create_and_borrow(cls, db, data):
        book = Book(**data.dict(exclude={"user_id"}))
        db.add(book)
        db.commit()
        return cls.borrow(db, data.user_id, book.id)

    @classmethod
    def borrow(cls, db, user_id, book_id):
        user = db.query(User).filter(User.id == user_id).first()
        book = db.query(Book).filter(Book.id == book_id).first()
        book.borrowers.append(user)
        db.commit()
        return book

    @classmethod
    def return_book(cls, db, user_id, book_id):
        user = db.query(User).filter(User.id == user_id).first()
        book = db.query(Book).filter(Book.id == book_id).first()
        book.borrowers.remove(user)
        db.commit()
        return book
