from selenium import webdriver
from selenium.webdriver import ChromeOptions
from time import sleep
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
"""
option.add_experimental_option('excludeSwitches', ['enable-automation']): 
这个选项用于移除命令行参数 enable-automation, 它告诉网站当前浏览器会话是由Seleni
um自动化工具控制的。移除这个参数可以使浏览器表现得更加像人类用户的手动操作。
    """
option.add_experimental_option('useAutomationExtension', False)
"""
option.add_experimental_option('useAutomationExtension', False): 
这会禁用Selenium的自动化扩展, 这个扩展通常会被一些网站用来检测Selenium控制。
    """
option.add_argument("--headless")
# 设置无头模式
browser = webdriver.Chrome(options=option)
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': 'Object.defineProperty(navigator, "webdriver", {get:() => undefined})'
})
"""
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {...}): 这个命令
会在浏览器打开每个新文档(即每个新页面)时执行指定的JavaScript代码。

'Object.defineProperty(navigator, "webdriver", {get:() =>- undefined})': 
这段JavaScript代码会重新定义navigator.webdriver属性的getter方法, 
使其返回undefined。这可以隐藏Selenium控制的事实, 因为一些网站会检查navigator.webdriver属性
来判断浏览器是否由Selenium驱动。
    """
browser.get('https://antispider1.scrape.center/')
sleep(5)
browser.get_screenshot_as_file('pornhub-tits.png')
browser.quit()
