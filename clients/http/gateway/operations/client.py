from httpx import Response, QueryParams
from locust.env import Environment

from clients.http.client import HTTPClient, HTTPClientExtensions
from clients.http.gateway.client import (build_gateway_http_client,
build_gateway_locust_http_client) # Импорт билдера для нагрузочного тестирования

from clients.http.gateway.operations.schema import (
    GetOperationsQuerySchema, GetOperationsResponseSchema,
    GetOperationQuerySchema, GetOperationResponseSchema,
    GetOperationReceiptResponseSchema,
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
    def get_operation_api(self, operation_id: str) -> Response:
        return self.get(f"/api/v1/operations/{operation_id}", extensions=HTTPClientExtensions(route="/api/v1/operations/{operation_id}"))

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}", extensions=HTTPClientExtensions(route="/api/v1/operations/operation-receipt/{operation_id}"))

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        return self.get("/api/v1/operations", params=QueryParams(**query.model_dump(by_alias=True)), extensions=HTTPClientExtensions(route="/api/v1/operations"))

    def get_operations_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query.model_dump(by_alias=True)), extensions=HTTPClientExtensions(route="/api/v1/operations/operations-summary"))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestSchema) -> Response:
        return self.post("/api/v1/operations/make-fee-operation", json=request.model_dump(by_alias=True))

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestSchema) -> Response:
        return self.post("/api/v1/operations/make-top-up-operation", json=request.model_dump(by_alias=True))

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestSchema) -> Response:
        return self.post("/api/v1/operations/make-cashback-operation", json=request.model_dump(by_alias=True))

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestSchema) -> Response:
        return self.post("/api/v1/operations/make-transfer-operation", json=request.model_dump(by_alias=True))

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        return self.post("/api/v1/operations/make-purchase-operation", json=request.model_dump(by_alias=True))

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestSchema) -> Response:
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request.model_dump(by_alias=True))

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestSchema) -> Response:
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request.model_dump(by_alias=True))

    # Все методы принимают card_id и account_id
    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseSchema:
        """Создаёт операцию комиссии (все поля генерируются автоматически)"""
        request = MakeFeeOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseSchema:
        """Создаёт операцию пополнения (все поля генерируются автоматически)"""
        request = MakeTopUpOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseSchema:
        """Создаёт операцию кэшбэка (все поля генерируются автоматически)"""
        request = MakeCashbackOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cashback_operation_api(request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseSchema:
        """Создаёт операцию перевода (все поля генерируются автоматически)"""
        request = MakeTransferOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseSchema:
        """Создаёт операцию покупки (amount, status и category генерируются автоматически)"""
        request = MakePurchaseOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseSchema:
        """Создаёт операцию оплаты счёта (все поля генерируются автоматически)"""
        request = MakeBillPaymentOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseSchema:
        """Создаёт операцию снятия наличных (все поля генерируются автоматически)"""
        request = MakeCashWithdrawalOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)

# Добавляем builder для OperationsGatewayHTTPClient
def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())

# Новый билдер для нагрузочного тестирования
def build_operations_gateway_locust_http_client(environment: Environment) -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient адаптированного под Locust.

    Клиент автоматически собирает метрики и передаёт их в Locust через хуки.
    Используется исключительно в нагрузочных тестах.

    :param environment: объект окружения Locust.
    :return: экземпляр OperationsGatewayHTTPClient с хуками сбора метрик.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_locust_http_client(environment))