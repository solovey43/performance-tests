from httpx import Response, QueryParams
from typing import TypedDict, Literal
from clients.http.client import HTTPClient


class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения списка операций пользователя.
    """
    accountId: str

class GetSummaryQueryDict(TypedDict):
    """
    Структура данных для получения статистики по операциям пользователя.
    """
    accountId: str

class MakeFeeOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции комиссии.
    """
    status: Literal["FAILED", "COMPLETED", "IN_PROGRESS", "UNSPECIFIED"]
    amount: float
    cardId: str
    accountId: str


class MakeTopUpOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции пополнения.
    """
    status: Literal["FAILED", "COMPLETED", "IN_PROGRESS", "UNSPECIFIED"]
    amount: float
    cardId: str
    accountId: str

class MakeCashbackOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции кэшбека.
    """
    status: Literal["FAILED", "COMPLETED", "IN_PROGRESS", "UNSPECIFIED"]
    amount: float
    cardId: str
    accountId: str

class MakeTransferOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции перевода.
    """
    status: Literal["FAILED", "COMPLETED", "IN_PROGRESS", "UNSPECIFIED"]
    amount: float
    cardId: str
    accountId: str

class MakePurchaseOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции покупки.
    """
    status: Literal["FAILED", "COMPLETED", "IN_PROGRESS", "UNSPECIFIED"]
    amount: float
    cardId: str
    accountId: str
    category: str

class MakeBillPaymentOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции оплаты по счету.
    """
    status: Literal["FAILED", "COMPLETED", "IN_PROGRESS", "UNSPECIFIED"]
    amount: float
    cardId: str
    accountId: str

class MakeCashWithdrawalOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции снятия наличных денег.
    """
    status: Literal["FAILED", "COMPLETED", "IN_PROGRESS", "UNSPECIFIED"]
    amount: float
    cardId: str
    accountId: str


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """
    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id.
        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение чека по операции по operation_id.
        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка операций пользователя.
        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations", params=query)

    def get_operations_summary_api(self, query: GetSummaryQueryDict) -> Response:
        """
        Получение статистики по операциям для определенного счета.
        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations/operations-summary", params=query)

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Создание операции комиссии.
        :param request: Данные для создания операции комиссии.
        :return: Объект httpx.Response.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Создание операции пополнения.
        :param request: Данные для создания операции пополнения.
        :return: Объект httpx.Response.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Создание операции кэшбека.
        :param request: Данные для создания операции кэшбека.
        :return: Объект httpx.Response.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Создание операции перевода.
        :param request: Данные для создания операции перевода.
        :return: Объект httpx.Response.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Создание операции покупки.
        :param request: Данные для создания операции покупки.
        :return: Объект httpx.Response.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Создание операции оплаты по счету.
        :param request: Данные для создания операции оплаты по счету.
        :return: Объект httpx.Response.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Создание операции снятия наличных денег.
        :param request: Данные для операции снятия наличных денег.
        :return: Объект httpx.Response.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)