from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

import pydantic


class DirFormatError(Exception):
    def __init__(self, value: int, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str
    current_user_id: int


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: int

    @pydantic.validator("dir")
    @classmethod
    def is_valid_dir(cls, value):
        chars = [-1, 0, 1]
        if value in chars:
            return value

        raise DirFormatError(value=value, message="Dir should be either -1, 0 or 1")
