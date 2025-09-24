from httpx import Response, QueryParams
from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.operations.schema import (
    GetOperationsQuerySchema, GetOperationsResponseSchema,
    GetOperationResponseSchema, GetOperationReceiptResponseSchema,
    GetOperationsSummaryQuerySchema, GetOperationsSummaryResponseSchema,
    MakeFeeOperationRequestSchema, MakeFeeOperationResponseSchema,
    MakeTopUpOperationRequestSchema, MakeTopUpOperationResponseSchema,
    MakeCashbackOperationRequestSchema, MakeCashbackOperationResponseSchema,
    MakeTransferOperationRequestSchema, MakeTransferOperationResponseSchema,
    MakePurchaseOperationRequestSchema, MakePurchaseOperationResponseSchema,
    MakeBillPaymentOperationRequestSchema, MakeBillPaymentOperationResponseSchema,
    MakeCashWithdrawalOperationRequestSchema, MakeCashWithdrawalOperationResponseSchema
)


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получает информацию об операции по её идентификатору.
        :param operation_id: Уникальный идентификатор операции.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получает чек по заданной операции.
        :param operation_id: Уникальный идентификатор операции.
        :return: Объект httpx.Response с чеком по операции.
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Получает список операций по счёту.
        :param query: Параметры запроса.
        :return: Объект httpx.Response с операциями по счёту.
        """
        return self.get("/api/v1/operations", params=QueryParams(**query.model_dump(by_alias=True)))

    def get_operations_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:
        """
        Получает сводную статистику операций по счёту.
        :param query: Параметры запроса.
        :return: Объект httpx.Response с агрегированной информацией.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query.model_dump(by_alias=True)))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestSchema) -> Response:
        """
        Создаёт операцию комиссии.
        :param request: Тело запроса с параметрами операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request.model_dump(by_alias=True))

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestSchema) -> Response:
        """
        Создаёт операцию пополнения счёта.
        :param request: Тело запроса с параметрами операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request.model_dump(by_alias=True))

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestSchema) -> Response:
        """
        Создаёт операцию начисления кэшбэка.
        :param request: Тело запроса с параметрами операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request.model_dump(by_alias=True))

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestSchema) -> Response:
        """
        Создаёт операцию перевода средств.
        :param request: Тело запроса с параметрами операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request.model_dump(by_alias=True))

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """
        Создаёт операцию покупки.
        :param request: Тело запроса с параметрами операции, включая категорию.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request.model_dump(by_alias=True))

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestSchema) -> Response:
        """
        Создаёт операцию оплаты счёта.
        :param request: Тело запроса с параметрами операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request.model_dump(by_alias=True))

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestSchema) -> Response:
        """
        Создаёт операцию снятия наличных средств.
        :param request: Тело запроса с параметрами операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request.model_dump(by_alias=True))

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        query = GetOperationsQuerySchema(account_id=account_id)  # ИСПРАВЛЕНО: account_id вместо accountId
        response = self.get_operations_api(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        response = self.get_operation_api(operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        response = self.get_operation_receipt_api(operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        query = GetOperationsSummaryQuerySchema(account_id=account_id)
        response = self.get_operations_summary_api(query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def make_fee_operation(self, card_id: str, account_id: str, amount: float = 55.77, status: str = "COMPLETED") -> MakeFeeOperationResponseSchema:
        request = MakeFeeOperationRequestSchema(
            status=status,
            amount=amount,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(self, card_id: str, account_id: str, amount: float, status: str = "COMPLETED") -> MakeTopUpOperationResponseSchema:
        request = MakeTopUpOperationRequestSchema(
            status=status,
            amount=amount,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(self, card_id: str, account_id: str, amount: float, status: str = "COMPLETED") -> MakeCashbackOperationResponseSchema:
        request = MakeCashbackOperationRequestSchema(
            status=status,
            amount=amount,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cashback_operation_api(request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(self, card_id: str, account_id: str, amount: float, status: str = "COMPLETED") -> MakeTransferOperationResponseSchema:
        request = MakeTransferOperationRequestSchema(
            status=status,
            amount=amount,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(self, card_id: str, account_id: str, amount: float, category: str, status: str = "COMPLETED") -> MakePurchaseOperationResponseSchema:
        request = MakePurchaseOperationRequestSchema(
            status=status,
            amount=amount,
            card_id=card_id,
            account_id=account_id,
            category=category
        )
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(self, card_id: str, account_id: str, amount: float, status: str = "COMPLETED") -> MakeBillPaymentOperationResponseSchema:
        request = MakeBillPaymentOperationRequestSchema(
            status=status,
            amount=amount,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str, amount: float, status: str = "COMPLETED") -> MakeCashWithdrawalOperationResponseSchema:
        request = MakeCashWithdrawalOperationRequestSchema(
            status=status,
            amount=amount,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)


# Добавляем builder для OperationsGatewayHTTPClient
def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
