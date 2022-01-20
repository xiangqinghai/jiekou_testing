import pytest
from common.yaml_util import yamlUtil





# 在执行test_contract_details用例时，先执行conn_database用例
@pytest.fixture(scope="function")
def conn_database():
    print("连接数据库")
    yield
    # // yield 类似teardown的功能 和return都是返回的意思，区别为：yield 返回多次及多个数据
    print("关闭数据库")

# 清除yaml数据
@pytest.fixture(scope="session",autouse=True)
# @pytest.fixture(scope="function",autouse=True)
def clear_yaml():
    yamlUtil().clear_relation_yaml()