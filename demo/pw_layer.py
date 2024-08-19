from playwright.sync_api import Page,expect,sync_playwright


# def pw1_baidu():
#     #主要包括下面四层: pw browser context page
#     pw= sync_playwright().start()         #需要引入sync_playwright这个实例
#     browser=pw.chromium.launch(headless=False)
#     context=browser.new_context()
#     page=context.new_page()
#     page.goto(url="https://www.baidu.com")
#     # page.wait_for_timeout(5_000)
#     page.locator('//input[@name="wd"]').fill("playwright")
#     page.get_by_text("百度一下").click()
#     expect(page.get_by_text("https://github.com/microsoft/playwright")).to_be_visible()
#     pw.stop()  #跑完之后stop接着跑下面的用例  相当于隔离   同步方法一个session里面只允许一个playwright实例
#
# def pw2_baidu():
#     #主要包括下面四层: pw browser context page
#     pw= sync_playwright().start()         #需要引入sync_playwright这个实例
#     browser=pw.chromium.launch(headless=False)
#     context=browser.new_context()
#     page=context.new_page()
#     page.goto(url="https://www.baidu.com")
#     # page.wait_for_timeout(5_000)
#     page.locator('//input[@name="wd"]').fill("playwright")
#     page.get_by_text("百度一下").click()
#     expect(page.get_by_text("https://github.com/microsoft/playwright")).to_be_visible()
#     pw.stop()

def pw1_baidu():
    #主要包括下面四层: pw browser context page
    # pw= sync_playwright().start()         #需要引入sync_playwright这个实例
    with sync_playwright() as pw:   #这样就不用在下面写stop了
        browser=pw.chromium.launch(headless=False)
        context=browser.new_context()
        page=context.new_page()
        page.goto(url="https://www.baidu.com")
        # page.wait_for_timeout(5_000)
        page.locator('//input[@name="wd"]').fill("playwright")
        page.get_by_text("百度一下").click()
        expect(page.get_by_text("https://github.com/microsoft/playwright")).to_be_visible()


def pw2_baidu():
    #主要包括下面四层: pw browser context page
    pw= sync_playwright().start()         #需要引入sync_playwright这个实例
    browser=pw.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto(url="https://www.baidu.com")
    # page.wait_for_timeout(5_000)
    page.locator('//input[@name="wd"]').fill("playwright")
    page.get_by_text("百度一下").click()
    expect(page.get_by_text("https://github.com/microsoft/playwright")).to_be_visible()
    pw.stop()

pw1_baidu()
pw2_baidu()