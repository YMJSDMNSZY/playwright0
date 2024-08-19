from testcases import *


# def test_login(page:Page):
#     login_page=登录页_类(page)
#     login_page.登录("winni","playwright001")
#     login_page


def test_login(page:Page):
    my_page=PageIns(page)
    my_page.登录页.登录("winni","playwright001")
    my_page