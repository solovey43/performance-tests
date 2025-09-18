import httpx
import time

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

print(f"user_id: {user_id}")
print(f"Status Code: {create_user_response.status_code}")
print(f"Response: {create_user_response_data}")

open_deposit_payload = {
    "userId": user_id
}

open_deposit_response = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-deposit-account",
    json=open_deposit_payload
)

open_deposit_response_data = open_deposit_response.json()

print(f"Status Code: {open_deposit_response.status_code}")
print(f"Response: {open_deposit_response_data}")
