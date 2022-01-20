import json

import pytest
import requests

from common.requests_util import RequestsUtil
from common.yaml_util import yamlUtil


class TestSendR:
    # 登录
    # 冒烟测试
    # @pytest.mark.smoke
    # def test_login(self):
    #     url = "http://172.16.11.40:8082/app/login"
    #     data = {"username": "admin", "password": "111111"}
    #     # 获取token值,post请求，返回结果转json，拿出data 下面的token
    #     to = requests.post(url=url, data=data).json()["data"]["token"]
    #     global token
    #     token = {"token": to}
    #     # token值写入yaml文件
    #     # yamlUtil().write_relation_yaml(token)
    #     print("登录测试成功")
    #     return token

    # 查询消息
    # yaml读取测试用例，使用read_testcase_yaml方法读取login_realte.yml文件中的数据；caseinfo表示测试用例的信息,读取的数据为字典格式,保存到caseinfo里面，然后传到test_query_message用例里面，打印/使用caseinfo里面的信息
    @pytest.mark.parametrize("caseinfo",yamlUtil().read_testcase_yaml("login_relate.yml"))
    def test_query_message(self,caseinfo):
        method = caseinfo["method"]
        url = caseinfo["url"]
        # 从yaml文件读取token值
        token = yamlUtil().read_relation_yaml()
        # 调用公共类方法RequestsUtil().send_request（）
        rep = RequestsUtil().send_request_nodata(method, url, headers=token)
        # text转换成json格式
        rep = json.loads(rep)
        # print(rep)
        # rep = requests.request(methon, url=url, headers=token)
        assert "state" in rep
        # print(rep.text)
        print("查询消息测试成功")
    # 阅读一条消息
    def test_read_message(self):
        token = yamlUtil().read_relation_yaml()
        url = "http://172.16.11.40:8082/app/readMsg"
        # yamlUtil().write_relation_yaml(url)
        data = {"msgId": 247}
        rep = requests.request("POST", url=url, data=data, headers=token)
        # 断言
        assert "state" in rep.text
        print(rep.text)
        print("阅读一条消息测试成功")


if __name__ == '__main__':
    pytest.main()