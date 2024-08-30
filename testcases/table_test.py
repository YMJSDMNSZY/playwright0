from testcases import *

def test_new_context(new_context):
    my_page_测试员=PageIns.login_and_return_page_with_new_context(new_context,"测试员")
    my_page_测试员.项目集.navigate()
    # index=my_page_测试员.项目集.主表格.get_header_index("开始时间")
    # loc=my_page_测试员.项目集.主表格.get_row_locator(my_page_测试员.page.get_by_text("table_test"))
    # my_page_测试员.项目集.主表格.get_cell("开始时间",my_page_测试员.page.get_by_text("table_test")).text_content()
    # my_page_测试员.项目集.主表格.get_cell(1,"table_test").text_content()
    # my_page_测试员.项目集.主表格.get_cell(1,-1).text_content()
    # my_page_测试员.项目集.主表格.get_cell(1,6).text_content()
    my_page_测试员.项目集.主表格.get_row_dict(1, 6)
    #my_page_测试员.项目集.主表格.get_row_dict(my_page_测试员.page.get_by_text("自动化创建项目集_1724231150858667600"))
    my_page_测试员