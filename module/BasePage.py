from module import *
from module.table import Table
from module.locators import Locators

class PageObject:
    def __init__(self, page: Page):
        self.page = page
        self.url = ""
        self.locators = Locators(self.page)

    def navigate(self):
        self.page.goto(self.url)

    def table(self,唯一文字,表格序号=-1):
        return Table(self.page,唯一文字,表格序号)

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

    def 表单_文本框填写(self,表单项名称:str,需要填写的文本:str,表单最上层定位:Locator=None, timeout: float = None):
        if 表单最上层定位:
            表单最上层定位.locator(self.locators.表单项中包含操作元素的最上级div(表单项名称)).locator(
                "input,textarea").locator("visible=true").last.fill(需要填写的文本, timeout=timeout)
        else:
            self.locators.表单项中包含操作元素的最上级div(表单项名称).locator("input,textarea").locator(
                "visible=true").last.fill(需要填写的文本, timeout=timeout)


