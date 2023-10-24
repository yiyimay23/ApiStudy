#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/4/11 16:41
# @Author :天草柑橘
# @File : yaml_util.py
# @Software: PyCharm
import os

import yaml


# 获取项目根目录
def get_object_path():
    return os.path.abspath(os.getcwd().split("commons")[0])

# 读取yaml文件
def read_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value

# 读取extract.yaml文件
def read_extract_yaml(key):
    with open(get_object_path() + "/extract.yaml", 'r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[key]

# 写入extract.yaml文件
def write_extract_yaml(data):
    with open(get_object_path() + "/extract.yaml", 'a', encoding='utf-8') as f:
        yaml.dump(data=data, stream=f, allow_unicode=True)

# 清除extract,yaml文件
def clear_extract_yaml():
    with open(get_object_path() + "/extract.yaml", 'w', encoding='utf-8') as f:
        f.truncate()

# 读取config.yaml文件
def read_config_yaml(one_nodo, two_node):
    with open(get_object_path() + "/config.yaml", 'r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[one_nodo][two_node]

# 读取数据的yaml
def read_data_yaml(yaml_path):
    with open(get_object_path() + yaml_path, 'r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value