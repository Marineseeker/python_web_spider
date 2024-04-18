from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
from time import sleep
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = Options()  
chrome_options.add_argument("--mute-audio")  # 添加静音参数  
browser = webdriver.Chrome(options=chrome_options)  

browser.get('https://mooc2-ans.chaoxing.com/mooc2-ans/mycourse/stu?courseid=200904037&clazzid=94493931&cpi=265656443&enc=f2e9fec7297d9b1658c2cfc53c981d23&t=1712839516208&pageHeader=1&v=2')
wait = WebDriverWait(browser,10)
input_phone = browser.find_element(By.CSS_SELECTOR, "#phone")
input_password = browser.find_element(By.CSS_SELECTOR, "#pwd")
input_phone.send_keys('19130603472')
input_password.send_keys('marine1235689412')
button = browser.find_element(By.CSS_SELECTOR, '#loginBtn')
button.click()
"""
wait = WebDriverWait(browser,10)
wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame_content")))
lesson = wait.until(
    EC.presence_of_element_located((
        By.CSS_SELECTOR, "#course_200904037_94493931 > div.course-info > h3 > a > span")))
lesson.click()
chapter =  WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#nav_43089 > a')))
chapter.click()
# 获取所有窗口句柄
all_handles = browser.window_handles
# 切换到新窗口
new_window_handle = [handle for handle in all_handles if handle != browser.current_window_handle][0]
browser.switch_to.window(new_window_handle)
# 等待新窗口加载完成"""

browser.switch_to.default_content()
wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame_content-zj")))

span_nodes = WebDriverWait(browser, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[@class="chapter_item"]//span[@class="bntHoverTips"]'))
)

if span_nodes:
    for span in span_nodes:
        text = browser.execute_script("return arguments[0].textContent", span).strip()
        if text == '已完成':
            print("该任务节点已完成")
        elif text == '1个待完成任务点':
            print("未完成任务节点已找到,  切换到学习页面")
            links = span.find_elements(By.XPATH, '../../../..//a[@class="clicktitle"]')
            if links:
                links[0].click()
            else:
                print("未找到链接")
            break
else:
    print("no node")
sleep(10)

"""div_elements =  WebDriverWait(browser, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[@class="chapter_item"]//span[text()="1个待完成任务点"]/ancestor::div[@class="chapter_item"]')))

for div_element in div_elements:
    a_elements = div_element.find_elements(By.XPATH, '//a[@class="clicktitle"]')
    a_elements[2].click()"""

browser.switch_to.default_content()
wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "iframe")))
wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "#ext-gen1050 > iframe")))
button = browser.find_element(By.CSS_SELECTOR, "#video > button").click()
sleep(4000)