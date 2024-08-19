from testcases import *


def test_baidu(page:Page,base_url):
    # baidu=Baidu(page)
    # baidu.baidu_search("playwright","https://github.com/microsoft/playwright")
    # baidu.搜索框.fill()


    my_page=PageIns(page)
    # my_page.百度.baidu_search("playwright","https://github.com/microsoft/playwright")


    print(base_url)
    print(GlobalMap().get("baseurl"))