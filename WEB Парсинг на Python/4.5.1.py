# Нужно извлечь названия товаров с 4-х страниц
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

headers = {'User-Agent': UserAgent().random}
response = requests.get(url='https://parsinger.ru/html/index3_page_1.html', headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
last_page = int(soup.find('div', class_='pagen').text.split()[-1])
all_name_items = {}
for page in range(1, last_page + 1):
    item_list = []
    response = requests.get(url=f'https://parsinger.ru/html/index3_page_{page}.html')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    name_items_page = soup.find_all('a', class_='name_item')
    [item_list.append(item.text) for item in name_items_page]
    all_name_items[f'{page} page'] = item_list
print(all_name_items)
