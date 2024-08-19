from testcases import *


def test_filelock1(page:Page):
    # baidu=Baidu(page)
    # baidu.baidu_search("playwright","https://github.com/microsoft/playwright")
    # baidu.搜索框.fill()


    my_page=PageIns(page)
    # with FileLock("lock.loc"):
    #     my_page.百度.baidu_search("playwright","https://github.com/microsoft/playwright")
    #     page.wait_for_timeout(10_000)
    with FileLock(get_path("/.temp/lock.loc")):
        my_page.百度.baidu_search("playwright","https://github.com/microsoft/playwright")
        # page.wait_for_timeout(10_000)
        global_map=GlobalMap()
        global_map.set("a",123)