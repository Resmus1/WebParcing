# Собрать все данные с карточек в файл json
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json


def parsing(url):
    """Парсит указаную страницу по указаным правилам"""
    headers = {'User-Agent': UserAgent().random}
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def collect_info(soup):
    """Собирает все данные с карточек"""
    name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
    price = [x.text for x in soup.find_all('p', class_='price')]
    print(description)
    return name, description, price


def create_zip(name, description, price):
    """Создается json список с собраными данными"""
    result_json = []
    for description, price, name in zip(description, price, name):
        result_json.append({
            'name': name,
            'brand': [x.split(': ')[1].strip() for x in description][0],
            'type': [x.split(':')[1].strip() for x in description][1],
            'connect': [x.split(': ')[1].strip() for x in description][2],
            'game': [x.split(': ')[1].strip() for x in description][3],
            'price': price,
        })
    return result_json


def create_json(result_json):
    """Создается json файл с собраными данными"""
    with open('res.json', 'w', encoding='utf-8') as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)
        print('Done')


base = parsing('https://parsinger.ru/html/index2_page_1.html')
list_name, list_description, list_price = collect_info(base)
result = create_zip(list_name, list_description, list_price)
create_json(result)
