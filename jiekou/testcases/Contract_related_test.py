import json
import random
import datetime
import time
import pytest
import requests
import os
from requests_toolbelt.multipart.encoder import MultipartEncoder
from common.yaml_util import yamlUtil


class Test_Contract:


    # 供应商-采购商（公司名称）下拉选项
    def test_supplier_purchaser(self, conn_database):
        data = {"type": 1}
        url = 'http://172.16.11.40:8082/app/contractCompanies'
        # global token
        # token = Token.token(self)
        # global token
        # # 从yaml文件读取token值
        token = yamlUtil().read_relation_yaml()
        response = requests.request("GET", url=url, headers=token, params=data)
        # 断言
        assert "state" in response.text
        # print(response.text)
        print("供应商-采购商（公司名称）下拉选项测试成功")

    # 销售 - 采购单个合同详情
    def test_contract_details(self):
        token = yamlUtil().read_relation_yaml()
        data = {"id": 17}
        url = 'http://172.16.11.40:8082/app/contractDetail'
        response = requests.request("GET", url=url, headers=token, params=data)
        # 断言
        assert "state" in response.text
        # print(response.text)
        print("销售-采购单个合同详情测试成功")

    # 销售 - 采购合同分页查询
    def test_paging_query(self):
        token = yamlUtil().read_relation_yaml()
        data = {"current": 1, "limit": 10, "type": 10}
        url = 'http://172.16.11.40:8082/app/contractList'
        response = requests.request("GET", url=url, headers=token, params=data)
        # 断言
        assert "state" in response.text
        # print(response.text)
        print("销售 - 采购合同分页查询测试成功")

    # 销售 - 采购合同统计
    def test_contract_statistics(self):
        token = yamlUtil().read_relation_yaml()
        data = {"type": 1}
        url = 'http://172.16.11.40:8082/app/contractStatistics'
        response = requests.request("GET", url=url, headers=token, params=data)
        # 断言
        assert "state" in response.text
        # print(response.text)
        print("销售-采购合同统计测试成功")
    # 单个文件上传
    def test_file_upload(self):
        url = "http://172.16.11.40:8082/file/upload"
        token = yamlUtil().read_relation_yaml()
        data = {"file": open(r"E:\HydProductTest\auttest\jiekou\File_upload\10.png", "rb")}
        rep = requests.request("POST", url, headers=token, files=data)
        global url_new
        url_new = rep.json()["data"]
        print(rep.text)
        print(url_new)
        print("上传文件成功")

    # 批量上传文件
    def test_batch_upload_files(self):
        url = "http://172.16.11.40:8082/file/uploadBatch"
        token = yamlUtil().read_relation_yaml()
        # file_1 = open(r"E:\HydProductTest\auttest\jiekou\File_upload\10.png", "rb")
        # file_2 = open(r"E:\HydProductTest\auttest\jiekou\File_upload\1.jpg", "rb")
        # data = [{file_1, file_2}]
        data = {"file0": open(r"E:\HydProductTest\auttest\jiekou\File_upload\1.jpg", "rb"),
                "file1": open(r"E:\HydProductTest\auttest\jiekou\File_upload\10.png", "rb"),
                "file2": open(r"E:\HydProductTest\auttest\jiekou\File_upload\2.jpg", "rb")
                }
        data = json.jumps(data)
        headers = {
            "Content-Type": "application/json",
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mzg2MTIwMjEsInVzZXJJZCI6MTgyLCJ1c2VybmFtZSI6IjEzMzMzMzMzMzMzIn0.X2EP7DvGecJyFmgN9cNgHbLPqr-QiyasmB8UbRYan_o"
        }
        rep = requests.request("POST", url, headers=headers, files=data)
        print(rep.text)
        print("批量上传文件成功")

        # 销售 - 采购合同添加
    def test_add_contract(self):
        token = yamlUtil().read_relation_yaml()
        code = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba',10))
        name = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba',10))
        type = random.randint(1, 2)
        # ghFile / 1638520389055 / 134.pdf
        data = {
                "code": code,
                "companyId": 2,
                "createTime": "",
                "id": 0,
                "images": "",
                "imagesList": ["ghFile/1638520441435/1.jpg"],
                "name": name,
                "pdfs": "",
                "pdfsList": [""],
                "type": type
                }
        url = "http://172.16.11.40:8082/app/contractAdd"
        response = requests.request("POST", url=url, headers=token, json=data)
        assert "state" in response.text
        print(data)
        print(response.text)
        print("销售-采购合同添加成功")




if __name__ == '__main__':
    pytest.main()
    os.system("allure generate ../temp -o ../reports --clean")









