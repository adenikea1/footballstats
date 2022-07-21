from covid_model import Covid

import requests

class Covid_stats():

    def __init__(self, stats):
        self.url = "https://disease.sh/v3/covid-19/all"+stats
        self.request = requests.get(self.url)
        self.resp_json = self.request.json()

    def covid_response(self):
        return Covid(self.resp_json)

        print(Covid(self.resp_json))