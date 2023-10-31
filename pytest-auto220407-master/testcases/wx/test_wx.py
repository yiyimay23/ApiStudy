#!C:\pythonCode
# -*- coding: utf-8 -*-
# @File : test_wx.py
# @Software: PyCharm

import allure
import pytest

from commons.parameterize_util import read_testcase_yaml
from commons.requests_util import RequestsUtil
from redloads.wx_fun import WxFun
from commons.logger_util import logs


@allure.feature('微信模块')  # 模块名称定制
class TestWx:

    @allure.story("获取接口统一鉴权码")
    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("./testcases/wx/get_token.yaml"))
    def test_get_token(self, caseinfo):
        res = RequestsUtil(WxFun()).standard_yaml(caseinfo)

    @allure.story("创建标签")
    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("./testcases/wx/create_flag.yaml"))
    def test_create_flag(self, caseinfo):
        res = RequestsUtil(WxFun()).standard_yaml(caseinfo)

    @allure.story("删除标签")
    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("./testcases/wx/delete_flag.yaml"))
    def test_delete_flag(self, caseinfo):
        res = RequestsUtil(WxFun()).standard_yaml(caseinfo)
        # logs("当上一步创建标签提示'errmsg'：'too many tag now, no need to add new hint'，会导致创建失败，从而‘删除标签’报错")


    @allure.story("获取公共号已创建的标签")
    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("./testcases/wx/select_flag.yaml"))
    def test_select_flag(self, caseinfo):
        res = RequestsUtil(WxFun()).standard_yaml(caseinfo)

    @allure.story("文件上传")
    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("./testcases/wx/file_upload.yaml"))
    def test_file_upload(self, caseinfo):
        res = RequestsUtil(WxFun()).standard_yaml(caseinfo)
