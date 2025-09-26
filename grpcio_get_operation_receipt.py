import grpc

from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import OpenDebitCardAccountRequest, OpenDebitCardAccountResponse
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (
    MakeTopUpOperationRequest,
    MakeTopUpOperationResponse)
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import (
GetOperationReceiptRequest,
GetOperationReceiptResponse)
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.operations.operation_pb2 import OperationStatus

from tools.fakers import fake

# Устанавливаем соединение с gRPC-сервером
channel = grpc.insecure_channel("localhost:9003")

# Создаём gRPC-клиенты для сервисов
users_gateway_service = UsersGatewayServiceStub(channel)
accounts_gateway_service = AccountsGatewayServiceStub(channel)
operations_gateway_service = OperationsGatewayServiceStub(channel)

# Формируем запрос на создание пользователя с рандомными данными
create_user_request = CreateUserRequest(
    email=fake.email(),
    last_name=fake.last_name(),
    first_name=fake.first_name(),
    middle_name=fake.middle_name(),
    phone_number=fake.phone_number()
)

# Отправляем запрос и получаем ответ
create_user_response: CreateUserResponse = users_gateway_service.CreateUser(create_user_request)
print('Create user response:', create_user_response)

# Создаем запрос на открытие дебетового счета
open_debit_card_account_request = OpenDebitCardAccountRequest(
    user_id=create_user_response.user.id,
)

open_debit_card_account_response: OpenDebitCardAccountResponse = accounts_gateway_service.OpenDebitCardAccount(open_debit_card_account_request)
print('Open debit card account response:', open_debit_card_account_response)

# Операция пополнения счета
make_top_up_operation_request = MakeTopUpOperationRequest(
    status = OperationStatus.OPERATION_STATUS_COMPLETED,
    amount = fake.amount(),
    card_id = open_debit_card_account_response.account.cards[0].id,
    account_id = open_debit_card_account_response.account.id
)

make_top_up_operation_response: MakeTopUpOperationResponse = operations_gateway_service.MakeTopUpOperation(make_top_up_operation_request)
print('Make top up operation response:', make_top_up_operation_response)

# Получение чека по операции
get_receipt_request = GetOperationReceiptRequest(
    operation_id=make_top_up_operation_response.operation.id
)

get_receipt_response: GetOperationReceiptResponse = operations_gateway_service.GetOperationReceipt(get_receipt_request)
print('Get operation receipt response:', get_receipt_response)
























