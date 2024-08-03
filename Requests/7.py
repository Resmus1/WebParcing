import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

headers = {'User-Agent': UserAgent().random}
response = requests.get(url='https://parsinger.ru/html/index1_page_1.html', headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
last_page = int(soup.find('div', class_='pagen').text.split()[-1])
all_cost = 0
for page in range(1, last_page + 1):
    list_href = []
    response = requests.get(url=f'https://parsinger.ru/html/index1_page_{page}.html')
    soup = BeautifulSoup(response.text, 'lxml')
    item = soup.find('div', class_='item_card')
    for i in item.find_all('a'):
        if i['href'] not in list_href:
            list_href.append(i['href'])
    for link in list_href:
        response = requests.get(url=f'https://parsinger.ru/html/{link}')
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        for i in soup.find('span', id='in_stock').text.split():
            if i.isdigit():
                stock = int(i)
        for i in soup.find('span', id='price').text.split():
            if i.isdigit():
                price = int(i)
        all_cost += price * stock
        print(all_cost)
