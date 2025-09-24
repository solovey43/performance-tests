from httpx import Response
from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.cards.schema import (
    IssuePhysicalCardResponseSchema,
    IssueVirtualCardResponseSchema,
    IssuePhysicalCardRequestSchema,
    IssueVirtualCardRequestSchema
)


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """

    def issue_virtual_card_api(self, request: IssueVirtualCardRequestSchema) -> Response:
        """
        Создание виртуальной карты.

        :param request: Данные для создания виртуальной карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request.model_dump(by_alias=True))

    def issue_physical_card_api(self, request: IssuePhysicalCardRequestSchema) -> Response:
        """
        Создание физической карты.

        :param request: Данные для создания физической карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request.model_dump(by_alias=True))

    def issue_virtual_card(self, user_id: str, account_id: str) -> IssueVirtualCardResponseSchema:
        """
        Создание виртуальной карты.

        :param user_id: ID пользователя
        :param account_id: ID аккаунта
        :return: Схема ответа с данными карты
        """
        request = IssueVirtualCardRequestSchema(
            user_id=user_id,
            account_id=account_id
        )
        response = self.issue_virtual_card_api(request)
        return IssueVirtualCardResponseSchema.model_validate_json(response.text)

    def issue_physical_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponseSchema:
        """
        Создание физической карты.

        :param user_id: ID пользователя
        :param account_id: ID аккаунта
        :return: Схема ответа с данными карты
        """
        request = IssuePhysicalCardRequestSchema(
            user_id=user_id,
            account_id=account_id
        )
        response = self.issue_physical_card_api(request)
        return IssuePhysicalCardResponseSchema.model_validate_json(response.text)


# Добавляем builder для CardsGatewayHTTPClient
def build_cards_gateway_http_client() -> CardsGatewayHTTPClient:
    return CardsGatewayHTTPClient(client=build_gateway_http_client())