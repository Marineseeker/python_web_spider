from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

browser = webdriver.Firefox()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'

browser.get(url)
browser.switch_to.frame('iframeResult')

source = browser.find_element(By.CSS_SELECTOR, '#draggable')
target = browser.find_element(By.CSS_SELECTOR, '#droppable')
"""这行代码在Selenium自动化脚本中的作用是切换到名为 `'iframeResult'` 
的`<iframe>`元素内部。`<iframe>`是一个内联框架, 它允许在当前HTML文档中嵌入另一个独立的HTML文档。
    """
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
"""actions.drag_and_drop 方法在 Selenium 中用于模拟一个元素被拖拽到另一个元素的位置的操作。
找到的 WebElement 对象。目标元素 (Target Element): 这是你想要将源元素拖拽到的位置。同
样，这也是一个 WebElement 对象。
    """
actions.perform()
browser.quit()