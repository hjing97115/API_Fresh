import configparser
import yaml
import os

# 当前文件完整目录
now_path = os.path.realpath(__file__)
# print(now_path)
# data.yaml完整目录
data_yaml_path = os.path.join(os.path.dirname(os.path.dirname(now_path)), "data", "data.yaml")
ini_path = os.path.join(os.path.dirname(os.path.dirname(now_path)), "config", "settings.ini")


class FileRead:
    def __init__(self):
        self.data_yaml_path = data_yaml_path
        self.ini_path = ini_path

    @staticmethod
    def read_data_yaml():
        with open(data_yaml_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            return data

    @staticmethod
    def read_ini():
        config = configparser.ConfigParser()
        config.read(ini_path, encoding='utf-8')
        return config


# base_data = FileRead()
# print(base_data)
# print(base_data.read_data_yaml())
# print(base_data.read_ini()['host']['api_sit_url'] + '/code/')

