# 读取yaml数据
import  os
import yaml

class yamlUtil:
    # 读取relation.yml文件数据  ;key作为读取的值
    def read_relation_yaml(self):
        # os.getcwd()获取当前根目录;mode="r" 读取【read的简称】;as f作为一个文件流
        with open(os.getcwd()+"/relation.yml",mode="r",encoding="utf-8")as f:
            # stream = f,加载文件流， Loader = yaml.FullLoader 加载方式，加载所有类型的方式
            value=yaml.load(stream=f,Loader=yaml.FullLoader)
            # 返回读取的数据
            return value;

     # 写入relation.yml文件数据
    def write_relation_yaml(self,data):
         # os.getcwd()获取当前根目录;mode="a" 追加;as f作为一个文件流
        with open(os.getcwd() + "/relation.yml", mode="a", encoding="utf-8")as f:
            # data,读取的数据，stream = f,加载文件流， allow_unicode=True 允许使用encoding编码格式
            yaml.dump(data=data, stream=f, allow_unicode=True )

     # 清除relation.yml文件数据
    def clear_relation_yaml(self):
        with open(os.getcwd() + "/relation.yml", mode="w", encoding="utf-8")as f:
            f.truncate()

    # def load(path):
    #     file = open(path, 'r', encoding='utf-8')
    #     data = yaml.load(file, Loader=yaml.FullLoader)
    #     return data

    # 读取测试用例
    def read_testcase_yaml(self,yaml_name):
        # os.getcwd()获取当前根目录;mode="r" 读取【read的简称】;as f作为一个文件流
        with open(os.getcwd()+"\\"+yaml_name,mode="r",encoding="utf-8")as f:
            # stream = f,加载文件流， Loader = yaml.FullLoader 加载方式，加载所有类型的方式
            value=yaml.load(stream=f,Loader=yaml.FullLoader)
            # 返回读取的数据
            return value;


