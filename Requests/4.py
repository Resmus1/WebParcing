# Вычисляем процент скидки по ценам с одним знаком после запятой
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

headers = {'User-agent': UserAgent().random}
response = requests.get(url='https://parsinger.ru/html/hdd/4/4_1.html', headers=headers)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
price_list = {'price': soup.find('span', id='price').text, 'old_price': soup.find('span', id='old_price').text}
for name, cost in price_list.items():
    price_list[name] = int(''.join(i if i.isdigit() else '' for i in cost))
print(round((price_list['old_price'] - price_list['price']) * 100 / price_list['old_price'], 1))
