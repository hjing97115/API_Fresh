# from requests import get

from core.rest_client import RestClient


class Api(RestClient):
    def __init__(self):
        super().__init__()

    @staticmethod
    def get_code(**kwargs):
        return RestClient.post("/code/", **kwargs)

    @staticmethod
    def register_mobile(**kwargs):
        return RestClient.post("/users/", **kwargs)



