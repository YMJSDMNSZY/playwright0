from module import *

class Table:
    def __init__(self,page:Page,唯一文字:str,表格序号:int=-1):
        self.page = page
        self.table_div=self.page.locator(".ant-table-container").filter(has_text=唯一文字).nth(表格序号)