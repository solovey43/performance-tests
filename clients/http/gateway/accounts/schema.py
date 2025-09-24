from pydantic import BaseModel, Field, ConfigDict, EmailStr
from enum import StrEnum
from clients.http.gateway.cards.schema import CardSchema


class AccountType(StrEnum):
    DEPOSIT = "DEPOSIT"
    SAVINGS = "SAVINGS"
    DEBIT_CARD = "DEBIT_CARD"
    CREDIT_CARD = "CREDIT_CARD"

class AccountStatus(StrEnum):
    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"
    PENDING_CLOSURE = "PENDING_CLOSURE"

class AccountSchema(BaseModel):
    id: str
    type: AccountType
    cards: list[CardSchema]
    status: AccountStatus
    balance: float


class GetAccountsQuerySchema(BaseModel):
    """
    Структура данных для получения списка счетов пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias="userId")


class GetAccountsResponseSchema(BaseModel):
    accounts: list[AccountSchema]


class OpenDepositAccountRequestSchema(BaseModel):
    """
    Структура данных для открытия депозитного счета.
    """
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias="userId")

class OpenDepositAccountResponseSchema(BaseModel):
    account: AccountSchema


class OpenSavingsAccountRequestSchema(BaseModel):
    """
    Структура данных для открытия сберегательного счета.
    """
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias="userId")

class OpenSavingsAccountResponseSchema(BaseModel):
    account: AccountSchema


class OpenDebitCardAccountRequestSchema(BaseModel):
    """
    Структура данных для открытия дебетового счета.
    """
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias="userId")

class OpenDebitCardAccountResponseSchema(BaseModel):
    account: AccountSchema


class OpenCreditCardAccountRequestSchema(BaseModel):
    """
    Структура данных для открытия кредитного счета.
    """
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias="userId")

class OpenCreditCardAccountResponseSchema(BaseModel):
    account: AccountSchema