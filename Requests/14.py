# Написать таблицу на сбор данных со всех 4-х страниц создать таблицу со значениями.
import csv
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


def parse_page(url):
    headers = {'User-Agent': UserAgent().random}
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
    prices = [x.text for x in soup.find_all('p', class_='price')]

    data = []
    for item, price, descr in zip(name, prices, description):
        flatten = [item, *[x.split(':')[1].strip() for x in descr if x], price]
        data.append(flatten)
    return data


with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование', 'Бренд', 'Форм-фактор', 'Емкость', 'Объем буферной памяти', 'Цена'])

    base_url = 'https://parsinger.ru/html/index4_page_{}.html'
    for i in range(1, 5):
        url = base_url.format(i)
        page_data = parse_page(url)

        for row in page_data:
            writer.writerow(row)

print('Файл создан')
