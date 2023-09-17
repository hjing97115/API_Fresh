
import pytest,  allure
from api.user_api import send_code, register
from test_cases.user_center.conftest import get_code
from utils.read_path import FileRead
from core.rest_client import api_root_url
from core.api_util import Api
from core.rest_client import RestClient
from api.api import test_json


@allure.feature("用户模块")
class TestUser:
    @allure.story("用户注册-发送验证码")
    @allure.title("注册手机号测试用例")
    def test_register(self):
        #   json_data = {"mobile": 15622283333}
        # 获取传参json
        json_data = FileRead.read_data_yaml()['test_register']

        # url = "http://admin.5istudy.online/code/"
        # print(json_data)
        # 返回结果
        result = send_code(json_data)
        # print(result)
        assert result.success is True

        # 获取手机号，取得短信验证码code
        mobile = result.body['mobile']
        code = get_code(mobile)
        print(code)
        print(mobile)
        register_result = register(code, mobile)



