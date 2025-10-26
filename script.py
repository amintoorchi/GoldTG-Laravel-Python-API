import requests

url = "https://tabangohar.com/GheymatKhan/prices_in_table.html"
response = requests.get(url)
data = response.json()
price = data["c"]

api_url = "https://example.com/api/store-price"
payload = {
    "price": price
}

r = requests.post(api_url, json=payload)

if r.status_code in [200, 201]:
    print("Price sent successfully!")
else:
    print("Failed to send price:", r.status_code, r.text)
