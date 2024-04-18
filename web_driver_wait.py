from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get('https://www.bilibili.com/')

wait = WebDriverWait(browser, 10)

input_bili = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="nav-searchform"]/div[1]/input')))
input_bili.send_keys('python')

button_bili = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav-searchform"]/div[2]')))
button_bili.click()

browser.execute_script('window.open()')
browser.switch_to.window(browser.window_handles[1])
browser.get('https://cn.pornhub.com/')

button_porn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/button')))
button_porn.click()

input_porn = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchInput"]')))
input_porn.send_keys('tits')
input_porn.send_keys(Keys.ENTER)
sleep(10)
browser.get_screenshot_as_file('pornhub-tits.png')
browser.quit()