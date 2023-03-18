import requests
import pandas as pd
from lxml import html

list_url = "https://www.horsetelex.com/pedigree/horses/find-by-properties"
individual_horse_url="https://www.horsetelex.com/pedigree/family/getFamily?id=2461132"
page_number = 1
results = []
for page_number in range (1,11):
  payload = {
    "name": None,
    "father": None,
    "mother": None,
    "fatherOfMother": None,
    "year": "2019",
    "studbook": None,
    "reg": None,
    "fei": None,
    "chipnumber": None,
    "page": f"{page_number}"
}
  headers = {
    "Content-Type": "application/json",
    "Cookie": "loginState=null; cookieConsent=%7B%22shareButtons%22%3A%7B%22title%22%3A%22Share%20Buttons%22%2C%22isAccepted%22%3Atrue%2C%22category%22%3A2%2C%22type%22%3A1%2C%22description%22%3A%22We%20need%20permission%20to%20communicate%20with%20foreign%20servers%20(Facebook%2C%20Twitter%2C%20etc.)%22%7D%2C%22googleAnalytics%22%3A%7B%22title%22%3A%22Statistics%20on%20the%20use%20of%20the%20application%22%2C%22description%22%3A%22We%20need%20the%20permission%20to%20create%20statistics%20about%20the%20usage%20of%20the%20application.%20This%20helps%20us%20to%20optimize%20the%20performance%20of%20the%20application%22%2C%22category%22%3A1%2C%22onlyBrowser%22%3Atrue%2C%22type%22%3A0%2C%22isAccepted%22%3Atrue%2C%22scriptUrl%22%3A%22https%3A%2F%2Fwww.googletagmanager.com%2Fgtag%2Fjs%3Fid%3DUA-23677259-20%22%2C%22position%22%3A0%2C%22onlyProdMode%22%3Atrue%7D%2C%22googleAnalytics2%22%3A%7B%22title%22%3A%22Statistics%20on%20the%20use%20of%20the%20application%22%2C%22description%22%3A%22We%20need%20the%20permission%20to%20create%20statistics%20about%20the%20usage%20of%20the%20application.%20This%20helps%20us%20to%20optimize%20the%20performance%20of%20the%20application%22%2C%22category%22%3A1%2C%22onlyBrowser%22%3Atrue%2C%22type%22%3A0%2C%22isAccepted%22%3Atrue%2C%22scriptUrl%22%3A%22%2Fpublic%2Fscripts%2Fgoogle-analytics-script.js%22%2C%22position%22%3A1%2C%22onlyProdMode%22%3Atrue%7D%7D; _ga=GA1.2.96005662.1678304766; _gid=GA1.2.1893307342.1678304766; _gat_gtag_UA_23677259_20=1"
}
  response = requests.request("POST", list_url, json=payload, headers=headers)
  data = response.json()
  for product in data['horses']:
    results.append(product)
print(len(results))
response = requests.request("GET", individual_horse_url)


response = requests.get(individual_horse_url)
print(response.json)


# horses_df = pd.json_normalize(results)
# horses_df.to_csv('first1000results.csv')
