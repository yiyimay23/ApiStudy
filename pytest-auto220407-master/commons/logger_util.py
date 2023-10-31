#!C:\pythonCode
# -*- coding: utf-8 -*-
# @File : logger_util.py.py
# @Software: PyCharm
import logging
import time
from builtins import int, str, Exception

from commons.yaml_util import get_object_path, read_config_yaml


class LoggerUtil:
    @staticmethod
    def create_log(logger_name="log"):
        logger = logging.getLogger(logger_name)
        # 设置全局的日志级别（从低到高：debug<info<warning<error<critical）
        logger.setLevel(logging.DEBUG)

        if not logger.handlers:
            # -------文件日志----------
            # 1.创建文件日志路径
            file_log_path = get_object_path() + "/logs/" + read_config_yaml("log", "log_name") + str(
                int(time.time())) + ".log"
            # 2.创建文件日志的控制器
            file_hander = logging.FileHandler(file_log_path, encoding='utf-8')
            # 3.创建文件日志的日志级别
            file_log_level = str(read_config_yaml("log", "log_level")).lower()
            if file_log_level == "debug":
                file_hander.setLevel(logging.DEBUG)
            elif file_log_level == "info":
                file_hander.setLevel(logging.INFO)
            elif file_log_level == "warning":
                file_hander.setLevel(logging.WARNING)
            elif file_log_level == "error":
                file_hander.setLevel(logging.ERROR)
            elif file_log_level == "critical":
                file_hander.setLevel(logging.CRITICAL)
            else:
                file_hander.setLevel(logging.DEBUG)
            # 4.创建文件日志格式
            file_hander.setFormatter(logging.Formatter(read_config_yaml("log", "log_format")))
            # 将文件日志的控制器加入到日志对象
            logger.addHandler(file_hander)
            # -------控制台日志----------
            # 1.创建控制台日志的控制器
            console_hander = logging.StreamHandler()
            # 2.创建控制台日志的日志级别
            console_log_level = str(read_config_yaml("log", "log_level")).lower()
            if console_log_level == "debug":
                console_hander.setLevel(logging.DEBUG)
            elif console_log_level == "info":
                console_hander.setLevel(logging.INFO)
            elif console_log_level == "warning":
                console_hander.setLevel(logging.WARNING)
            elif console_log_level == "error":
                console_hander.setLevel(logging.ERROR)
            elif console_log_level == "critical":
                console_hander.setLevel(logging.CRITICAL)
            else:
                console_hander.setLevel(logging.DEBUG)
            # 3.创建控制台日志格式
            console_hander.setFormatter(logging.Formatter(read_config_yaml("log", "log_format")))
            # 将控制台日志的控制器加入到日志对象
            logger.addHandler(console_hander)

        # 返回包含有文件日志控制器和控制台控制器的日志对象
        return logger


# 错误日志的输出
def error_log(message):
    LoggerUtil().create_log().error(message)
    raise Exception(message)


# 信息日志的输出
def logs(message):
    LoggerUtil().create_log().info(message)
