# Проходимся по страницам, заходим в каждый товар берем и складываем артикул.
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

headers = {'User-Agent': UserAgent().random}
response = requests.get(url='https://parsinger.ru/html/index3_page_4.html', headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
last_page = int(soup.find('div', class_='pagen').text.split()[-1])
sum_art = 0
for page in range(1, last_page + 1):
    list_href = []
    response = requests.get(url=f'https://parsinger.ru/html/index3_page_{page}.html')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find('div', class_='item_card')
    for i in items.find_all('a'):
        if i['href'] not in list_href:
            list_href.append(i['href'])
    for link in list_href:
        response = requests.get(url=f'https://parsinger.ru/html/{link}').text
        soup = BeautifulSoup(response, 'lxml')
        for i in soup.find('p', class_='article').text.split():
            if i.isdigit():
                sum_art += int(i)
print(sum_art)
