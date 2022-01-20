
import requests

from common.yaml_util import yamlUtil


class Login_out:
    def test_login(self):
        url = "http://172.16.11.40:8082/app/login"
        data = {"username": "admin", "password": "111111"}
        # 获取token值,post请求，返回结果转json，拿出data 下面的token
        to = requests.post(url=url, data=data).json()["data"]["token"]
        global token
        token = {"token": to}
        # token值写入yaml文件
        yamlUtil().write_relation_yaml(token)
        print("登录测试成功")
        # return token

