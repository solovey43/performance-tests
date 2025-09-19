import httpx
import time

# создать юзера
create_user_payload = {
    "email": f"user.{int(time.time())}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

user_id = create_user_response_data['user']['id']

# открыть кредитную карту
open_credit_card_payload = {
    "userId": user_id
}

open_credit_response = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-credit-card-account",
    json=open_credit_card_payload
)

open_credit_response_data = open_credit_response.json()
account_id = open_credit_response_data['account']['id']
card_id = open_credit_response_data['account']['cards'][0]['id']

# операция покупки
make_purchase_operation_payload = {
    "status": "IN_PROGRESS",
    "amount": 77.99,
    "cardId": card_id,
    "accountId": account_id,
    "category": "taxi"
}

make_purchase_operation_response = httpx.post(
    "http://localhost:8003/api/v1/operations/make-purchase-operation",
    json=make_purchase_operation_payload
)
make_purchase_operation_response_data = make_purchase_operation_response.json()

operation_id = make_purchase_operation_response_data['operation']['id']

get_receipt = httpx.get(f"http://localhost:8003/api/v1/operations/operation-receipt/{operation_id}")

print(f"Receipt data: {get_receipt.json()}")

