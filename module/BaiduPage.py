from module import PageObject,expect



class Baidu(PageObject):
    def __init__(self, page):
        super().__init__(page)
        self.url="https://www.baidu.com"
        self.search_input=self.page.locator("//input[@id='kw']")
        self.搜索框 = self.page.locator("//input[@id='kw']")
        self.百度一下 = self.page.locator("#su")


    def baidu_search(self,search_keyword,search_result):
        self.navigate()
        self.search_input.fill(search_keyword)
        self.百度一下.click()
        expect(self.page.get_by_text(search_result)).to_be_visible()

