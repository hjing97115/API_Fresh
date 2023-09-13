# from requests import get

from core.rest_client import RestClient


class Api(RestClient):
    def __init__(self):
        super().__init__()

    # @staticmethod
    def get_code(self, **kwargs):
        return self.post("/code/", **kwargs)