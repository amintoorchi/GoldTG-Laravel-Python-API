import requests

url = "https://tg"
response = requests.get(url)
data = response.json()
price = data["c"]

api_url = "https://example.com/api/store-price"
payload = {
    "price": price
}

r = requests.post(api_url, json={"price": price}, timeout=10, headers={"User-Agent": "PythonPriceBot/1.0"})

if r.status_code in [200, 201]:
    print("Price sent successfully!")
else:
    print("Failed to send price:", r.status_code, r.text)
