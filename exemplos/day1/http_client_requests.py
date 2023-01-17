import requests

result = requests.get("http://example.com/index.html")
print(result.status_code)
print(result.headers)
print(result.content)