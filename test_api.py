import requests
import json

# Teste da API
url = "http://localhost:8000/genres/6/"
data = {"name": "Ficção"}

# Teste com diferentes encodings
print("Testando com requests...")

try:
    response = requests.put(url, json=data, headers={'Content-Type': 'application/json; charset=utf-8'})
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Erro: {e}")

# Teste manual do JSON
print("\n" + "="*50)
print("Testando encoding do JSON...")
json_str = json.dumps(data, ensure_ascii=False)
print(f"JSON string: {json_str}")
print(f"JSON bytes: {json_str.encode('utf-8')}")
