import os.path

from filelock import FileLock
from playwright.sync_api import BrowserContext, Browser
from utils.GetPath import get_path

from module import *

from utils.globalMap import GlobalMap


class PageObject:
    def __init__(self, page: Page):
        self.page = page
        self.url = ""

    def navigate(self):
        self.page.goto(self.url)

    def click_button(self, button_name, timeout=30_000):
        button_loc = self.page.locator("button")
        for 单字符 in button_name:
            button_loc = button_loc.filter(has_text=单字符)

        button_loc.click(timeout=timeout)
        # self.page.get_by_role("button").filter(has_text=button_name).click(timeout=timeout)


    def search(self,搜索内容:str,placeholder=None):
        if placeholder:
            self.page.locator(f"//span[@class='ant-input-affix-wrapper']//input[contains(@placeholder,'{placeholder}')]").fill(搜索内容)
        else:
            self.page.locator(".ant-input-affix-wrapper input").fill(搜索内容)
        self.page.wait_for_load_state("networkidle")



    # @staticmethod
def login_and_return_page_with_new_context(new_context, 用户别名):
    from module.PageInstance import PageIns as PI
    from data_module.auth_Data import MyData
    from utils.GetPath import get_path
    global_map = GlobalMap()
    被测环境 = global_map.get("env")
    用户名 = MyData().userinfo(被测环境, 用户别名)["username"]
    密码 = MyData().userinfo(被测环境, 用户别名)["password"]
    with FileLock(get_path(f".temp/{被测环境}-{用户别名}.lock")):
        if os.path.exists(get_path(f".temp/{被测环境}-{用户别名}.json")):
            context: BrowserContext = new_context(storage_state=get_path(f".temp/{被测环境}-{用户别名}.json"))
            page = context.new_page()
            my_page = PI(page)
            my_page.我的任务.navigate()
            expect(my_page.登录页.用户名输入框.or_(my_page.登录页.通知铃铛)).to_be_visible()
            if my_page.登录页.用户名输入框.count():
                my_page.登录页.登录(用户名,密码)
                my_page.page.context.storage_state(path=get_path(f".temp/{被测环境}-{用户别名}.json"))
        else:
            context: BrowserContext = new_context()
            page = context.new_page()
            my_page = PI(page)
            my_page.登录页.登录(用户名,密码)
            my_page.page.context.storage_state(path=get_path(f".temp/{被测环境}-{用户别名}.json"))

    return my_page
