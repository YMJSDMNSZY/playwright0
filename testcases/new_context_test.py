from testcases import *

  #可用两种方式
# def test_new_context(new_context):
#     context1:BrowserContext=new_context(storage_state="winni.json")
#     context1.new_page().goto("/workbench/myapproval")
#     context2: BrowserContext = new_context()
#     context2.new_page().goto("/workbench/myapproval")
#     context2


@pytest.mark.browser_context_args(storage_state="winni.json")
def test_new_context(page:Page):
    page.goto("/workbench/myapproval")
    page