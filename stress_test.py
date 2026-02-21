import requests
import random
from datetime import datetime, timedelta
import time

BASE_URL = "http://localhost:5477/blackrock/challenge/v1/returns:index"

print("Generating 100,000 transactions...")

base = datetime(2023, 1, 1)

transactions = [
    {
        "date": (base + timedelta(seconds=i)).strftime("%Y-%m-%d %H:%M:%S"),
        "amount": random.randint(1, 5000)
    }
    for i in range(300000)
]

payload = {
    "age": 30,
    "wage": 50000,
    "inflation": 5.5,
    "q": [],
    "p": [],
    "k": [
        {
            "start": "2023-01-01 00:00:00",
            "end": "2023-12-31 23:59:59"
        }
    ],
    "transactions": transactions
}

print("Sending request...")

start = time.time()
response = requests.post(BASE_URL, json=payload)
end = time.time()

print("Status Code:", response.status_code)
print("Execution Time (client side):", round(end - start, 2), "seconds")
print("Response length:", len(response.text))