import requests

# 1. گرفتن قیمت از سایت
url = "https://tabangohar.com/GheymatKhan/prices_in_table.html"
response = requests.get(url)
data = response.json()
price = data["c"]

# 2. فرستادن به API لاراول
api_url = "https://example.com/api/store-price"
payload = {
    "price": price
}

r = requests.post(api_url, json=payload)

if r.status_code == 200:
    print("Price sent successfully!")
else:
    print("Failed to send price. Status code:", r.status_code)
