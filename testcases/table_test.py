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
    # my_page_测试员.项目集.主表格.get_row_dict(1, 6)
    #my_page_测试员.项目集.主表格.get_row_dict(my_page_测试员.page.get_by_text("自动化创建项目集_1724231150858667600"))
    my_page_测试员.项目集.主表格.get_col_dict("项目集名称")

    # my_page_测试员.项目集.表单_文本框填写("项目集名称", "123456")
    # my_page_测试员.项目集.表单_文本框填写("项目集名称1", "123456", timeout=2_000)
    # my_page_测试员.项目集.表单_文本框填写("项目集名称1", "123456", timeout=2_000)
    # my_page_测试员.项目集.表单_文本框填写("项目集名称", "12345678",my_page_测试员.page.locator('//*[@class="ant-form ant-form-horizontal"]'))
    # my_page_测试员.项目集.表单_文本框填写("项目描述", "收到就好部分没拿到")

    # my_page_测试员.项目集.表单_下拉框选择("父项目集", "公共项目集")

    #my_page_测试员.项目集.表单_radio选择("权限类型","企业内公开")

    my_page_测试员.项目集.表单_switch开关("自动生成README文件", "是")




    my_page_测试员