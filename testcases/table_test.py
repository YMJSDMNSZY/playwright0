from testcases import *

def test_new_context(new_context):
    my_page_测试员=PageIns.login_and_return_page_with_new_context(new_context,"测试员")
    my_page_测试员.项目集.navigate()
    my_page_测试员.项目集.主表格.get_header_index("项目集名称")
    my_page_测试员.项目集.主表格.get_row_locator(my_page_测试员.page.get_by_text("自动化创建项目集_1724231092840667600")).highlight()
    my_page_测试员