from playwright.sync_api import Page,expect,Browser,BrowserContext

# from module.BaiduPage import Baidu
# from module.登录页 import 登录页_类

from module.PageInstance import PageIns
import pytest
from filelock import FileLock
from utils.GetPath import get_path
from utils.globalMap import GlobalMap
from module.BasePage import PageObject,login_and_return_page_with_new_context
from module import *
