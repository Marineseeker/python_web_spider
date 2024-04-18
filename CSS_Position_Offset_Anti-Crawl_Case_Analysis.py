from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import re

def parse_name(name_html):
    """接受h3标题的html文本"""
    has_whole = name_html('.whole')
    if has_whole:
        return name_html.text()
    else:
        chars = name_html('.char')
        """定位到class为char的span节点"""
        items = []
        for char in chars.items():
            items.append({
                'text': char.text().strip(),
                'left': int(re.search(r'(\d+)px', char.attr('style')).group(1))
                # 提取span标签的left属性值，并转换为int类型
            })
        items = sorted(items, key=lambda x: x['left'], reverse=False)
        # 按left属性值排序 
        # sorted(iterable, key=None, reverse=False)
        return ''.join([item.get('text') for item in items])
        # 按left属性值排序后的文本列表，使用join方法拼接成字符串

def parse_name_beatiful(name_html):
    """直接接受网站html"""
    soup = BeautifulSoup(name_html, 'html.parser')
    h3_elements = soup.find_all('h3', class_='m-b-sm name')
    list_text = []
    for h3 in h3_elements:
        spans = h3.find_all('span')
        chars = [(span.find('font').text.strip(), int(span['style'].split(':')[1].replace('px;', ''))) for span in spans]
        sorted_chars = sorted(chars, key=lambda x: x[1])
        text = ''.join([char[0] for char in sorted_chars])
        list_text.append(text)
    return list_text

def parse_name_beatiful_h3(name_html):
    """接受h3标题的html文本"""
    has_whole = pq(name_html)('.whole')
    if has_whole:
        return pq(name_html).text()
    else:
        list_text = []
        # 使用Beautiful Soup解析HTML
        soup = BeautifulSoup(name_html, 'html.parser')
        # 选择h3标签中的所有span标签，并按left属性值排序
        spans = soup.select('h3 span')
        spans.sort(key=lambda span: int(span['style'].split(':')[1].replace('px;', '')))
        # 从排序后的span标签中提取文本 
        text = ''.join(span.text.strip() for span in spans)
        return text

browser = webdriver.Chrome()
browser.get('https://antispider3.scrape.center/')
WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.item')))
html=browser.page_source
doc=pq(html)
names=doc('.item .name')
for name_html in names.items():
    name = parse_name(name_html)
    print(name)
browser.close()