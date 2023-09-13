
import requests, allure
from utils.read_path import base_data
from core.rest_client import api_root_url
from core.api_util import Api


@allure.feature("用户模块")
class TestUser:
    @allure.story("用户注册-发送验证码")
    @allure.title("注册手机号测试用例")
    def test_register(self):
        # json_data = {"mobile": 15622283333}
        json_data = base_data.read_data_yaml()['test_register']
        # print(json_data)
        # send_code(json_data)
        ged_code = Api()
        response = ged_code.get_code(json=json_data)
        print(response.status_code)

