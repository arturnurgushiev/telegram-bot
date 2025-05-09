import requests


class CurrencyAPI:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_currency_data(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get data from API: {response.status_code}")
