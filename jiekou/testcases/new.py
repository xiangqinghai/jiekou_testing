# import requests
# from requests_toolbelt import  MultipartEncoder
#
#
#
# data = '{"code": "123","companyId": 8,"createTime": "","imagesList": ["fileName":{"png图片.png}"],"name": "132","pdfsList": [ "fileName": "pdf文件.pdf}"],"type": 1}'
# url = 'http://172.16.11.40:8082/app/contractAdd'
# file_path1 = open("../File_upload/1.jpg", 'rb')
# file_path2 = open("../File_upload/1.pdf", 'rb')
# m = MultipartEncoder(fields={"contract": data, 'imagesList': ('png图片.png', file_path1), 'pdfsList': ('pdf文件.pdf', file_path2)})
# token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mzg1OTgzMDIsInVzZXJJZCI6MTgyLCJ1c2VybmFtZSI6IjEzMzMzMzMzMzMzIn0.pdJ2ddj8nA2bStBwJEZgrObxmyCcnonRtENBn45WnGY"
# response = requests.post(url=url,data=m, headers={'Content-Type': m.content_type, token: token}).json()
# print(response)


# import requests
# data = {
#                 "code": 'dkfbd',
#                 "companyId": 2,
#                 "createTime": "",
#                 "id": 0,
#                 "images": "",
#                 "imagesList": ["E:/HydProductTest/auttest/jiekou/File_upload/1.jpg"],
#                 "name": 'jhvfk',
#                 "pdfs": "",
#                 "pdfsList": ["E:/HydProductTest/auttest/jiekou/File_upload/1.pdf"],
#                 "type":1
#                 }
# token = {"token ": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mzg1OTgzMDIsInVzZXJJZCI6MTgyLCJ1c2VybmFtZSI6IjEzMzMzMzMzMzMzIn0.pdJ2ddj8nA2bStBwJEZgrObxmyCcnonRtENBn45WnGY"}
# url = 'http://172.16.11.40:8082/app/contractAdd'
# response = requests.request("POST", url=url, headers=token, data=data)
# print(response.text)
# Contract_related_test.py::Test_Contract::test_add_contract {'id': 0, 'companyId': 2, 'name': 'hsebujnqvf', 'type': 1, 'createTime': '', 'code': 'gimzbyvpnl', 'pdfsList': [], 'imagesList': ['ghFile/1638520129649/1.jpg'], 'images': '', 'pdfs': ''}