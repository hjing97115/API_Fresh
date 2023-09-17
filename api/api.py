from core import api_util


def test_json(json_data):
    """
    # 测试json传参
    :param json_data:
    :return:
    """
    response = api_util.Api.post_data(json=json_data)