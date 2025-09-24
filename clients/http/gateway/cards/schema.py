from pydantic import BaseModel, Field, ConfigDict, EmailStr
from enum import StrEnum

class CardType(StrEnum):
    VIRTUAL = "VIRTUAL"
    PHYSICAL = "PHYSICAL"

class CardStatus(StrEnum):
    ACTIVE = "ACTIVE"
    FROZEN = "FROZEN"
    CLOSED = "CLOSED"
    BLOCKED = "BLOCKED"

class CardPaymentSystem(StrEnum):
    VISA = "VISA"
    MASTERCARD = "MASTERCARD"


class CardSchema(BaseModel):
    id: str
    pin: str
    cvv: str
    type: CardType
    status: CardStatus
    account_id: str = Field(alias="accountId")
    card_number: str = Field(alias="cardNumber")
    card_holder: str = Field(alias="cardHolder")
    expiry_date: str = Field(alias="expiryDate")
    payment_system: CardPaymentSystem = Field(alias="paymentSystem")


class IssueVirtualCardRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    """
    Структура данных для создания виртуальной карты.
    """
    user_id: str = Field(alias="userId")
    account_id: str = Field(alias="accountId")

class IssueVirtualCardResponseSchema(BaseModel):
    card: CardSchema


class IssuePhysicalCardRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    """
    Структура данных для создания физической карты.
    """
    user_id: str = Field(alias="userId")
    account_id: str = Field(alias="accountId")

class IssuePhysicalCardResponseSchema(BaseModel):
    card: CardSchema