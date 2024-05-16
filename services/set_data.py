import random
import time

import requests
import json


data = []
url = "http://127.0.0.1:8000/api/product/"


headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE3NDMxMDczLCJpYXQiOjE3MTQ4MzkwNzMsImp0aSI6ImJiYmFiMDAzNDU3MTQxOGU4OTE2NTllZjJmODlhYjkxIiwidXNlcl9pZCI6MX0.VGF28sG0h27CjdQlLxm9k-joBtmwzMyOhcy9diYGzW8'
}


with open("data3.json", "r+", encoding='UTF-8') as jsonFile:
    data = json.load(jsonFile)

for item in data:
    payload = json.dumps({
      "name": item['name'],
      "img": item['img'],
      "price": item['price'],
      "description": item['description'],
      "quantity": random.randint(1, 100),
      "type": item['type']
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    time.sleep(0.3)
