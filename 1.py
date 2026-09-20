import os
import requests

print(os.getcwd())

for file in os.listdir():
    print(file)

url = "https://www.google.com"
response = requests.get(url)
print(response)