from grpc import Channel

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.cards.rpc_issue_virtual_card_pb2 import IssueVirtualCardRequest, IssueVirtualCardResponse
from contracts.services.gateway.cards.rpc_issue_physical_card_pb2 import IssuePhysicalCardRequest, IssuePhysicalCardResponse
from contracts.services.gateway.cards.cards_gateway_service_pb2_grpc import CardsGatewayServiceStub


class CardsGatewayGRPCClient(GRPCClient):
    """
    gRPC-клиент для взаимодействия с CardsGatewayService.
    Предоставляет высокоуровневые методы для выпуска виртуальных и физических карт.
    """
    def __init__(self, channel: Channel):
        """
        Инициализация клиента с указанным gRPC-каналом.

        :param channel: gRPC-канал для подключения к CardsGatewayService.
        """
        super().__init__(channel)

        self.stub = CardsGatewayServiceStub(channel)  # gRPC-стаб, сгенерированный из .proto

    def issue_virtual_card_api(self, request: IssueVirtualCardRequest) -> IssueVirtualCardResponse:
        """Низкоуровневый метод для отправки сырого gRPC-запроса на выпуск виртуальной карты"""
        return self.stub.IssueVirtualCard(request)

    def issue_physical_card_api(self, request: IssuePhysicalCardRequest) -> IssuePhysicalCardResponse:
        """Низкоуровневый метод для отправки сырого gRPC-запроса на выпуск физической карты"""
        return self.stub.IssuePhysicalCard(request)

    def issue_virtual_card(self, user_id: str, account_id: str) -> IssueVirtualCardResponse:
        """Высокоуровневый метод для выпуска виртуальной карты с заполнением обязательных полей"""
        request = IssueVirtualCardRequest(user_id=user_id, account_id=account_id)
        return self.issue_virtual_card_api(request)

    def issue_physical_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponse:
        """Высокоуровневый метод для выпуска физической карты с заполнением обязательных полей"""
        request = IssuePhysicalCardRequest(user_id=user_id, account_id=account_id)
        return self.issue_physical_card_api(request)

def build_cards_gateway_grpc_client() -> CardsGatewayGRPCClient:
    """
    Фабрика для создания экземпляра CardsGatewayGRPCClient.

    :return: Инициализированный клиент для CardsGatewayService.
    """
    return CardsGatewayGRPCClient(channel=build_gateway_grpc_client())