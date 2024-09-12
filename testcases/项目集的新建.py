import pytest

from testcases import *


# def test_项目集的新建(new_context):
#     my_page_测试员=login_and_return_page_with_new_context(new_context,"测试员")
#     my_page_测试员.项目集.创建项目集()
#
#
# # @pytest.fixture
# # def 删除项目集(new_context):
# #     #因为没有开始动作，所以直接yield就行
# #     yield
# #     my_page_测试员 = login_and_return_page_with_new_context(new_context, "测试员")
# #     my_page_测试员.项目集.删除项目集("自动化创建项目集")

@用例名称("项目集的新建")
@用例描述("""
1. 项目集的新建
2. 删除项目集
创建人: Carlymilo
""")
@用例级别(严重)
# def test_项目集的新建(new_context):
def test_项目集的新建(new_context, 删除项目集):
    with 测试步骤("初始化和登录测试员"):
        my_page_测试员=PageIns.login_and_return_page_with_new_context(new_context,"测试员")
    with 测试步骤("创建项目集"):
        my_page_测试员.项目集.创建项目集()


@pytest.fixture
def 删除项目集(new_context):
    yield
    with 测试步骤("初始化和登录测试员"):
        my_page_测试员 = PageIns.login_and_return_page_with_new_context(new_context, "测试员")
    with 测试步骤("删除创建的项目集"):
        my_page_测试员.项目集.删除项目集("自动化创建项目集")