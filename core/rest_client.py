import json

import requests

from utils.log_util import logger
from utils.read_path import FileRead

# 获取测试url
api_root_url = FileRead.read_ini()['host']['api_sit_url']
# print(api_root_url)


class RestClient():
    def __init__(self):
        self.api_root_url = api_root_url

    @staticmethod
    def get(url, **kwargs):
        return RestClient.request(url, "GET",  **kwargs)

    @staticmethod
    def post(url, **kwargs):
        return RestClient.request(url, "POST", **kwargs)

    @staticmethod
    def put(url, **kwargs):
        return RestClient.request("PUT", **kwargs)

    @staticmethod
    def delete(url, **kwargs):
        return RestClient.request(url, "DELETE", **kwargs)

    # 判断请求方法
    @staticmethod
    def request(url, method, **kwargs):
        RestClient.request_log(url, method, **kwargs)
        if method == "GET":
            return requests.get(api_root_url + url, **kwargs)
        if method == "POST":
            return requests.post(api_root_url + url, **kwargs)
        if method == "PUT":
            return requests.put(api_root_url + url, **kwargs)
        if method == "DELETE":
            return requests.delete(api_root_url + url, **kwargs)

    # 打印请求日志
    @staticmethod
    def request_log(url, method, **kwargs):
        data = dict(**kwargs).get("data")
        json_data = dict(**kwargs).get("json")
        params = dict(**kwargs).get("params")
        headers = dict(**kwargs).get("headers")

        logger.info("接口请求的地址>>>{}".format(api_root_url + url))
        logger.info("接口请求的方法>>>{}".format(method))
        if data is not None:
            logger.info("接口请求的data参数>>>\n{}".format(json.dumps(data, indent=2)))
        if json_data is not None:
            logger.info("接口请求的data参数>>>\n{}".format(json.dumps(json_data, indent=2)))
        if params is not None:
            logger.info("接口请求的data参数>>>\n{}".format(json.dumps(params, indent=2)))
        if headers is not None:
            logger.info("接口请求的data参数>>>\n{}".format(json.dumps(headers, indent=2)))