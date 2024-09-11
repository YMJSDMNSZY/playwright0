from testcases import *

def test_标单测试_自动填写表单(new_context):
    my_page_测试员=PageIns.login_and_return_page_with_new_context(new_context,"测试员")
    my_page_测试员.项目集.navigate()
    my_page_测试员.项目集.click_button("新建")
    my_page_测试员.项目集.快捷操作_填写表单(项目集名称="test123", 项目集周期="0,365", 父项目集="公共项目集")
    my_page_测试员