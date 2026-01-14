from httpx import Response, QueryParams
from locust.env import Environment

from clients.http.client import HTTPClient, HTTPClientExtensions
from clients.http.gateway.client import (build_gateway_http_client,
                                         build_gateway_locust_http_client)

from clients.http.gateway.operations.schema import (
    GetOperationsQuerySchema, GetOperationsResponseSchema,
    GetOperationQuerySchema, GetOperationResponseSchema,
    GetOperationsReceiptQuerySchema, GetOperationReceiptResponseSchema,
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
    # НИЗКОУРОВНЕВЫЕ API-МЕТОДЫ (работа с сырыми HTTP-ответами)

    def get_operation_api(self, query: GetOperationQuerySchema) -> Response:
        """
        Получить информацию об операции через query-параметры.
        Согласно схеме, operation_id передается как query-параметр.
        """
        return self.get(
            "/api/v1/operations",
            params=QueryParams(**query.model_dump(by_alias=True)),
            extensions=HTTPClientExtensions(route="/api/v1/operations")
        )

    def get_operation_receipt_api(self, query: GetOperationsReceiptQuerySchema) -> Response:
        """
        Получить чек операции через query-параметры.
        Согласно схеме, operation_id передается как query-параметр.
        """
        return self.get(
            "/api/v1/operations/operation-receipt",
            params=QueryParams(**query.model_dump(by_alias=True)),
            extensions=HTTPClientExtensions(route="/api/v1/operations/operation-receipt")
        )

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Получить список операций для конкретного счёта.
        Согласно схеме, принимает только account_id.
        """
        return self.get(
            "/api/v1/operations",
            params=QueryParams(**query.model_dump(by_alias=True)),
            extensions=HTTPClientExtensions(route="/api/v1/operations")
        )

    def get_operations_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:
        """
        Получить сводную информацию по операциям счёта.
        Согласно схеме, принимает только account_id.
        """
        return self.get(
            "/api/v1/operations/operations-summary",
            params=QueryParams(**query.model_dump(by_alias=True)),
            extensions=HTTPClientExtensions(route="/api/v1/operations/operations-summary")
        )

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

    # БИЗНЕС-МЕТОДЫ (высокоуровневые, возвращают валидированные схемы)

    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        """
        Получить информацию об операции по её идентификатору.

        Args:
            operation_id: Идентификатор операции

        Returns:
            Валидированная схема с информацией об операции
        """
        query = GetOperationQuerySchema(operation_id=operation_id)
        response = self.get_operation_api(query)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        """
        Получить чек операции по её идентификатору.

        Args:
            operation_id: Идентификатор операции

        Returns:
            Валидированная схема с информацией о чеке операции
        """
        query = GetOperationsReceiptQuerySchema(operation_id=operation_id)
        response = self.get_operation_receipt_api(query)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        """
        Получить список операций для конкретного счёта.

        Args:
            account_id: Идентификатор счёта

        Returns:
            Валидированная схема со списком операций
        """
        query = GetOperationsQuerySchema(account_id=account_id)
        response = self.get_operations_api(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        """
        Получить сводную информацию по операциям счёта.

        Args:
            account_id: Идентификатор счёта

        Returns:
            Валидированная схема со сводной информацией об операциях
        """
        query = GetOperationsSummaryQuerySchema(account_id=account_id)
        response = self.get_operations_summary_api(query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseSchema:
        """
        Создать операцию комиссии.

        Args:
            card_id: Идентификатор карты
            account_id: Идентификатор счёта

        Returns:
            Валидированная схема с информацией о созданной операции комиссии
        """
        request = MakeFeeOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseSchema:
        """
        Создать операцию пополнения.

        Args:
            card_id: Идентификатор карты
            account_id: Идентификатор счёта

        Returns:
            Валидированная схема с информацией о созданной операции пополнения
        """
        request = MakeTopUpOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseSchema:
        """
        Создать операцию кэшбэка.

        Args:
            card_id: Идентификатор карты
            account_id: Идентификатор счёта

        Returns:
            Валидированная схема с информацией о созданной операции кэшбэка
        """
        request = MakeCashbackOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cashback_operation_api(request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseSchema:
        """
        Создать операцию перевода.

        Args:
            card_id: Идентификатор карты
            account_id: Идентификатор счёта

        Returns:
            Валидированная схема с информацией о созданной операции перевода
        """
        request = MakeTransferOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseSchema:
        """
        Создать операцию покупки.

        Args:
            card_id: Идентификатор карты
            account_id: Идентификатор счёта

        Returns:
            Валидированная схема с информацией о созданной операции покупки
        """
        request = MakePurchaseOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseSchema:
        """
        Создать операцию оплаты счёта.

        Args:
            card_id: Идентификатор карты
            account_id: Идентификатор счёта

        Returns:
            Валидированная схема с информацией о созданной операции оплаты счёта
        """
        request = MakeBillPaymentOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(self, card_id: str,
                                       account_id: str) -> MakeCashWithdrawalOperationResponseSchema:
        """
        Создать операцию снятия наличных.

        Args:
            card_id: Идентификатор карты
            account_id: Идентификатор счёта

        Returns:
            Валидированная схема с информацией о созданной операции снятия наличных
        """
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