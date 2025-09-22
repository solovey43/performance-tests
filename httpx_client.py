import httpx
import time

# Исправлены заголовки
client = httpx.Client(
    base_url="http://localhost:8003",
    timeout=100,
    headers={'Authorization': 'Bearer 332'}  # Исправлено
)

payload = {
    "email": f"user.{int(time.time())}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

response = client.post("/api/v1/users", json=payload)

print(response.text)
print(response.request.headers)

client.close()