import requests

SERVER = "http://127.0.0.1:5000"

response = requests.get(SERVER + "/menu")
menu = response.json()
print("Latest Menu")
print(menu)

order = {"item": "Poha", "quantity": 2}
response = requests.post(
    SERVER + "/order",
    json=order
)
result = response.json()
print("Order Result:")
print(result)