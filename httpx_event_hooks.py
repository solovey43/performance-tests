import httpx

def request_hook(request: httpx.Request):
    print(f"Запрос: {request.method} {request.url}")

client = httpx.Client(event_hooks={"request": [request_hook]})
response = client.get("https://example.com")
