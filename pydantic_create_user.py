import uuid
from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, HttpUrl, EmailStr, ValidationError


# Добавили модель UserSchema
class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")

# Добавили модель запроса на создание пользователя
class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


# Добавили модель ответа с данными созданного пользователя
class CreateUserResponseSchema(BaseModel):
    user: UserSchema