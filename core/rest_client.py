import requests

from utils.read_path import base_data

api_root_url = base_data.read_ini()['host']['api_sit_url'] + '/code/'
# print(url)


class RestClient():
    def __init__(self):
        self.api_root_url = api_root_url

    @staticmethod
    def get(url, **kwargs):
        return requests.get(url, "GET",  **kwargs)


    def post(self, url, **kwargs):
        return self.request(url, "POST", **kwargs)

    def request(self, url, method, **kwargs):
        if method == "POST":
            return requests.post(self.api_root_url + url, **kwargs)