from pydantic import BaseModel, Field, ConfigDict, EmailStr
from tools.fakers import fake


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")

class GetUserResponseSchema(BaseModel):
    user: UserSchema


class CreateUserRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    """
    Структура данных для создания нового пользователя.
    """
    email: EmailStr = Field(default_factory=fake.email)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str = Field(alias="middleName", default_factory=fake.middle_name)
    phone_number: str = Field(alias="phoneNumber", default_factory=fake.phone_number)

class CreateUserResponseSсhema(BaseModel):
    user: UserSchema

