import time
from DrissionPage import WebPage
#ChromiumOptions类用于设置浏览器启动参数：
from DrissionPage import ChromiumOptions
# #SessionOptions类用于设置Session对象启动参数：
# from DrissionPage import SessionOptions
# #Settings用于设置全局配置：
# from DrissionPage.common import Settings
# #动作链，用于模拟一系列键盘和鼠标的操作：
# from DrissionPage.common import ActionChains
# #键盘按键类，用于键入 ctrl、alt 等按键：
# from DrissionPage.common import Keys
# #与 selenium 一致的By类，便于项目迁移：
# from DrissionPage.common import By
# #浏览器数据包监听器，用法详见“进阶使用”章节：
# from DrissionPage.common import Listener, RequestMan
# #easy_set里保存了一些便捷的 ini 文件设置方法，可选择使用：
# from DrissionPage.easy_set import *
# #异常放在以下路径：
# from DrissionPage.errors import ElementNotFoundError

from DrissionPage.easy_set import set_paths
#set_paths(browser_path=r'C:\Users\zhangjian\AppData\Local\Google\Chrome\Application\chrome.exe')
#set_paths(browser_path=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')

# 指定s模式创建对象
co = ChromiumOptions()
co.set_timeouts(implicit=10,pageLoad=3,script=2)
page = WebPage()
page.get('https://vip.anjuke.com')
time.sleep(3)
page('text:账号登录').click()
time.sleep(1)
page.ele('#loginAccount').click()
page.ele('#loginAccount').input("18842393575")
page.ele('#loginPwd').click()
page.ele('#loginPwd').input("Aa123456")
time.sleep(1)
page.ele('xpath://*[@id="main-root"]/div/div[1]/div[2]/div/div/div[1]/form/div[5]/input').click()
time.sleep(3)
cookies = page.get_cookies()
# 使用列表推导式构造字符串
result_string = ';'.join([f'{item["name"]}={item["value"]}' for item in cookies])
# 输出构造好的字符串
print(result_string)
time.sleep(1)


