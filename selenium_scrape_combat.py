from selenium import webdriver
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import urljoin
import logging 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

INDEX_URL = 'http://spa2.scrape.center/page/{page}'
TIME_OUT = 10
TOTAL_PAGE = 10

browser = webdriver.Chrome()
wait = WebDriverWait(browser, TIME_OUT)

def scrape_page(url, condition, locator):
    """通用的爬取方法"""
    logging.info('scrapeing %s', url)
    try:
        browser.get(url)
        wait.until(condition(locator))
    except TimeoutException:
        logging.error('error occurred while scraping %s', url, exc_info = True)

def scrape_index(page):
    """检测列表页是否可以爬取"""
    url = INDEX_URL.format(page = page)
    scrape_page(url, condition=EC.visibility_of_all_elements_located, locator=(By.CSS_SELECTOR, '#index .item'))
    
def parsel_index():
    """解析详情页URL"""
    elements = browser.find_elements(By.CSS_SELECTOR, '#index .item .name')
    """css_selector中的'#index .item .name'用于定位到一个列表页中所有详情页的url"""
    for element in elements:
        herf = element.get_attribute('href')
        yield urljoin(INDEX_URL, herf)

def scrape_detail(url):
    """检测详情页是否可以爬取"""
    scrape_page(url, condition=EC.visibility_of_all_elements_located, locator=(By.TAG_NAME, 'h2'))
    
def parsel_detail():
    """解析详情页数据"""
    url = browser.current_url
    name = browser.find_element(By.TAG_NAME, 'h2')
    catagories = [element.text for element in browser.find_elements(By.CSS_SELECTOR, '.catagories button sapan')]
    cover = browser.find_element(By.CSS_SELECTOR, '.cover').get_attribute('src')
    score = browser.find_element(By.CLASS_NAME, 'score').text
    drama = browser.find_element(By.CSS_SELECTOR, '.drama p').text
    return {
        'url':url,
        'name':name, 
        'catagories':catagories,
        'cover':cover, 
        'score':score, 
        'drama':drama
    }
    
def main():
    try:
        for page in range(1, TOTAL_PAGE+1):
            scrape_index(page)
            detail_urls = parsel_index()
            for detail_url in list(detail_urls):
                logging.info('get detail url %s',detail_url)
                scrape_detail(detail_url)
                detail_data = parsel_detail()
                logging.info('detail data %s', detail_data)
    finally:
        browser.quit()

if __name__ == '__main__':
    main()