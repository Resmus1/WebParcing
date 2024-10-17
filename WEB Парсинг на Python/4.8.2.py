# Напишите код, который собирает данные со всех страниц и категорий на сайте тренажере и сохраните всё в таблицу
import csv
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


def parce_page(page):
    """Парсит страницу"""
    headers = {'User-Agent': UserAgent().random}
    response = requests.get(page, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
    price = [x.text for x in soup.find_all('p', class_='price')]

    data = []
    for item, price, descr in zip(name, price, description):
        flatten = [item, *[x.split(':')[1].strip() for x in descr if x], price]
        data.append(flatten)
    return data


with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    write = csv.writer(file, delimiter=';')

    base_url = 'https://parsinger.ru/html/index{}_page_{}.html'
    for j in range(1, 6):
        for i in range(1, 5):
            url = base_url.format(j, i)
            page_data = parce_page(url)

        for row in page_data:
            write.writerow(row)

print('Файл создан')
