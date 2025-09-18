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

print(f"Status Code: {create_user_response.status_code}")
print(f"Response: {create_user_response_data}")

get_user_response = httpx.get(f"http://localhost:8003/api/v1/users/{create_user_response_data['user']['id']}")
get_user_response_data = get_user_response.json()
print(f"Status Code: {get_user_response.status_code}")
print(f"Response: {get_user_response_data}")




