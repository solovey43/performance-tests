from httpx import Response
from typing import TypedDict
from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class DocumentDict(TypedDict):
    url: str
    document: str

class GetTariffDocumentResponseDict(TypedDict):
    tariff: DocumentDict

class GetContractDocumentResponseDict(TypedDict):
    contract: DocumentDict

class DocumentsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/documents сервиса http-gateway.
    """

    def get_tariff_document_api(self, account_id: str) -> Response:
        """
        Получить документ тарифа по счету.
        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/documents/tariff-document/{account_id}")

    def get_contract_document_api(self, account_id: str) -> Response:
        """
        Получить документ контракта по счету.
        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/documents/contract-document/{account_id}")

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseDict:
        """
        Получить документ тарифа по счету.
        :param account_id: Идентификатор счета.
        :return: Распарсенный ответ от сервера.
        """
        response = self.get_tariff_document_api(account_id)
        return response.json()

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseDict:
        """
        Получить документ контракта по счету.
        :param account_id: Идентификатор счета.
        :return: Распарсенный ответ от сервера.
        """
        response = self.get_contract_document_api(account_id)
        return response.json()


# Добавляем builder для DocumentsGatewayHTTPClient
def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    return DocumentsGatewayHTTPClient(client=build_gateway_http_client())