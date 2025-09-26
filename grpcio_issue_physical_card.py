import grpc

from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
from contracts.services.gateway.users.rpc_get_user_pb2 import GetUserRequest, GetUserResponse
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from contracts.services.gateway.accounts.rpc_open_credit_card_account_pb2 import (
    OpenCreditCardAccountRequest,
    OpenCreditCardAccountResponse)
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub
from contracts.services.gateway.cards.rpc_issue_physical_card_pb2 import (
    IssuePhysicalCardRequest,
    IssuePhysicalCardResponse)
from contracts.services.gateway.cards.cards_gateway_service_pb2_grpc import CardsGatewayServiceStub
from tools.fakers import fake  # Используем генератор фейковых данных, созданный ранее


# Устанавливаем соединение с gRPC-сервером по адресу localhost:9003
channel = grpc.insecure_channel("localhost:9003")

# Создаём stub'ы (клиентские обёртки) для взаимодействия с соответствующими gRPC-сервисами
users_gateway_service = UsersGatewayServiceStub(channel)
cards_gateway_service = CardsGatewayServiceStub(channel)
accounts_gateway_service = AccountsGatewayServiceStub(channel)

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

# Создаем запрос на открытие кредитного счета
open_credit_card_account_request = OpenCreditCardAccountRequest(
    user_id=create_user_response.user.id,
)


open_credit_card_account_response: OpenCreditCardAccountResponse = accounts_gateway_service.OpenCreditCardAccount(open_credit_card_account_request)
print('Open credit card account response:', open_credit_card_account_response)

# Создаем запрос на выпуск физической карты
issue_physical_card_request = IssuePhysicalCardRequest(
    user_id=create_user_response.user.id,
    account_id=open_credit_card_account_response.account.id
)

issue_physical_card_response: IssuePhysicalCardResponse = cards_gateway_service.IssuePhysicalCard(issue_physical_card_request)
print('Issue physical card response:', issue_physical_card_response)
