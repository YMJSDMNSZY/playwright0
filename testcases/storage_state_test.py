from testcases import *


# def test_storage_state(page:Page):
#     my_page=PageIns(page)
#     my_page.登录页.登录("winni","playwright001")
#     my_page.page.context.storage_state(path="winni.json")

def test_storage_state(browser:Browser):
    context = browser.new_context(storage_state="winni.json")
    page = context.new_page()
    page.goto("https://playwright.ezone.work/workbench/workCalendar?date=20240723&viewType=calendar&viewUnit=month")
    page