import requests
import json

covid = requests.get("https://disease.sh/v3/covid-19/all")

resp = covid.json()
print(resp['deaths'])
print(covid.status_code)
print(covid.headers)
print(covid.content)
