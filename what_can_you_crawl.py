from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
try:
    browser.get("https://cn.pornhub.com/")
    button = browser.find_element(By.CSS_SELECTOR, '.contentMtubes > button:nth-child(4)')
    button.click()
    input_box = browser.find_element(By.CSS_SELECTOR, '.searchInput')
    input_box.send_keys('tits')
    input_box.send_keys(Keys.ENTER)
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.videoBox')))
    videos = browser.find_elements(By.CSS_SELECTOR, '.videoBox')
    for video in videos:
        title = video.find_element(By.CSS_SELECTOR, '.title > a').text
        views = video.find_element(By.CSS_SELECTOR, '.views').text
        print(f"{title} - {views}")
finally:
    browser.quit()
    