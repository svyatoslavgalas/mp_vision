import requests


class Parser:
    headers = {
        'Authorization': ''
    }

    def __init__(self, api_key):
        self.api_key = api_key

    def parse_items(self):
        self.headers['Authorization'] = self.api_key
        response = requests.get(
            f'https://suppliers-api.wildberries.ru/api/v2/stocks?take=99999&skip=0',
            headers=self.headers
        )
        return response.json()

    def parse_orders(self, take=10, skip=0):
        self.headers['Authorization'] = self.api_key
        response = requests.get(
            f'https://suppliers-api.wildberries.ru/api/v2/orders?date_start=2010-01-01T00:00:00Z&take=1000&skip=0',
            headers=self.headers
        )
        return response.json()


