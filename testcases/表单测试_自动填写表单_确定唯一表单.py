from testcases import *


def test_表单测试_自动填写表单_确定唯一表单(new_context):
    my_page_测试员 = PageIns.login_and_return_page_with_new_context(new_context, "测试员")
    my_page_测试员.项目集.navigate()
    my_page_测试员.项目集.click_button("新建")
    新建项目 = 项目集数据类_新建项目集(项目集名称="test123", 项目集周期="0,365", 父项目集="公共项目集")
    my_page_测试员.项目集.快捷操作_填写表单(**新建项目.as_dict(), timeout=5_000)
    my_page_测试员.项目集.快捷操作_填写表单_增加根据数据类确定唯一表单版(**新建项目.as_dict())
    # 新建项目temp = 项目集数据类_新建项目集_temp(项目集名称="test456", 项目集周期="0,7", 父项目集="公共项目集")
    # my_page_测试员.项目集.快捷操作_填写表单_增加根据数据类确定唯一表单版(**新建项目temp.as_dict())
    my_page_测试员
