from pydantic import BaseModel, Field, ConfigDict, EmailStr

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
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")

class CreateUserResponseSсhema(BaseModel):
    user: UserSchema


