from httpx import Response, QueryParams
from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.accounts.schema import (
    GetAccountsResponseSchema,
    GetAccountsQuerySchema,
    OpenDepositAccountRequestSchema,
    OpenDepositAccountResponseSchema,
    OpenSavingsAccountRequestSchema,
    OpenSavingsAccountResponseSchema,
    OpenDebitCardAccountRequestSchema,
    OpenDebitCardAccountResponseSchema,
    OpenCreditCardAccountRequestSchema,
    OpenCreditCardAccountResponseSchema
)


class AccountsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/accounts сервиса http-gateway.
    """

    def get_accounts_api(self, query: GetAccountsQuerySchema) -> Response:
        """
        Выполняет GET-запрос на получение списка счетов пользователя.

        :param query: Параметры запроса.
        :return: Объект httpx.Response с данными о счетах.
        """
        return self.get("/api/v1/accounts", params=QueryParams(**query.model_dump(by_alias=True)))

    def open_deposit_account_api(self, request: OpenDepositAccountRequestSchema) -> Response:
        """
        Выполняет POST-запрос для открытия депозитного счёта.

        :param request: Данные для открытия счёта.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/accounts/open-deposit-account", json=request.model_dump(by_alias=True))

    def open_savings_account_api(self, request: OpenSavingsAccountRequestSchema) -> Response:
        """
        Выполняет POST-запрос для открытия сберегательного счёта.

        :param request: Данные для открытия счёта.
        :return: Объект httpx.Response.
        """
        return self.post("/api/v1/accounts/open-savings-account", json=request.model_dump(by_alias=True))

    def open_debit_card_account_api(self, request: OpenDebitCardAccountRequestSchema) -> Response:
        """
        Выполняет POST-запрос для открытия дебетовой карты.

        :param request: Данные для открытия счёта.
        :return: Объект httpx.Response.
        """
        return self.post("/api/v1/accounts/open-debit-card-account", json=request.model_dump(by_alias=True))

    def open_credit_card_account_api(self, request: OpenCreditCardAccountRequestSchema) -> Response:
        """
        Выполняет POST-запрос для открытия кредитной карты.

        :param request: Данные для открытия счёта.
        :return: Объект httpx.Response.
        """
        return self.post("/api/v1/accounts/open-credit-card-account", json=request.model_dump(by_alias=True))

    def get_accounts(self, user_id: str) -> GetAccountsResponseSchema:
        """
        Получить список счетов пользователя.

        :param user_id: ID пользователя
        :return: Схема ответа со списком счетов
        """
        query = GetAccountsQuerySchema(user_id=user_id)
        response = self.get_accounts_api(query)
        return GetAccountsResponseSchema.model_validate_json(response.text)

    def open_deposit_account(self, user_id: str) -> OpenDepositAccountResponseSchema:
        """
        Открыть депозитный счёт.

        :param user_id: ID пользователя
        :return: Схема ответа с данными счёта
        """
        request = OpenDepositAccountRequestSchema(user_id=user_id)
        response = self.open_deposit_account_api(request)
        return OpenDepositAccountResponseSchema.model_validate_json(response.text)

    def open_savings_account(self, user_id: str) -> OpenSavingsAccountResponseSchema:
        """
        Открыть сберегательный счёт.

        :param user_id: ID пользователя
        :return: Схема ответа с данными счёта
        """
        request = OpenSavingsAccountRequestSchema(user_id=user_id)
        response = self.open_savings_account_api(request)
        return OpenSavingsAccountResponseSchema.model_validate_json(response.text)

    def open_debit_card_account(self, user_id: str) -> OpenDebitCardAccountResponseSchema:
        """
        Открыть дебетовый карточный счёт.

        :param user_id: ID пользователя
        :return: Схема ответа с данными счёта
        """
        request = OpenDebitCardAccountRequestSchema(user_id=user_id)
        response = self.open_debit_card_account_api(request)
        return OpenDebitCardAccountResponseSchema.model_validate_json(response.text)

    def open_credit_card_account(self, user_id: str) -> OpenCreditCardAccountResponseSchema:
        """
        Открыть кредитный карточный счёт.

        :param user_id: ID пользователя
        :return: Схема ответа с данными счёта
        """
        request = OpenCreditCardAccountRequestSchema(user_id=user_id)
        response = self.open_credit_card_account_api(request)
        return OpenCreditCardAccountResponseSchema.model_validate_json(response.text)


# Добавляем builder для AccountsGatewayHTTPClient
def build_accounts_gateway_http_client() -> AccountsGatewayHTTPClient:  # Исправлено имя функции
    return AccountsGatewayHTTPClient(client=build_gateway_http_client())