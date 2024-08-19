
from testcases import *



# def test_login(page:Page):
#     login_page=登录页_类(page)
#     login_page.登录("winni","playwright001")
#     login_page


def test_new_context(new_context):
    my_page_测试员=login_and_return_page_with_new_context(new_context,"测试员")
    my_page_项目经理=login_and_return_page_with_new_context(new_context,"项目经理")
    my_page_测试员.page
    my_page_测试员.登录页.登录()