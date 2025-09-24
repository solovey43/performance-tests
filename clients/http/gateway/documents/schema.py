from pydantic import BaseModel, Field, ConfigDict, EmailStr, HttpUrl
from enum import StrEnum
from clients.http.gateway.cards.schema import CardSchema

class DocumentSchema(BaseModel):
    url: HttpUrl
    document: str

class GetTariffDocumentResponseSchema(BaseModel):
    tariff: DocumentSchema

class GetContractDocumentResponseSchema(BaseModel):
    contract: DocumentSchema