from module import *

class Table:
    def __init__(self,page:Page,唯一文字:str,表格序号:int=-1):
        self.page = page
        self.page.wait_for_load_state("networkidle")
        self.table_div=self.page.locator(".ant-table-container").filter(has_text=唯一文字).nth(表格序号)
        self.table_header_tr=self.table_div.locator("//thead/tr")


    def get_header_index(self,表头文字:str)->int:
        return self.table_header_tr.locator("th").all_text_contents().index(表头文字)

    def get_row_locator(self,行定位元素:Locator)->Locator:
        return self.table_div.locator("tr").filter(has=行定位元素)