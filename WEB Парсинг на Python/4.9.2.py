# Собрать данные со всех 5 категорий на сайте.
# (Позволил для автоматизации вписать русские ключи,
# но при желании и необходимости можно поставить модуль или написать словарь для преобразования текста.)
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json


def parsing(url):
    """Парсит указанную страницу"""
    headers = {'User-Agent': UserAgent().random}
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def collect_url_list(full_url, soup):
    """Собирает список ссылок для парсинга"""
    url_list = []
    link_list = soup.find('div', class_='nav_menu').find_all('a')
    for lnk in link_list:
        url_list.append(full_url.split('index')[0] + lnk.get('href'))
    return url_list


def collect_info(soup):
    """Собирает все данные с карточек"""
    name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
    price = [x.text for x in soup.find_all('p', class_='price')]

    return name, description, price


def parse_description(description):
    """Преобразует данные из карточек в словарь"""
    result_dict = []
    for item in description:
        item_dict = {}
        for attribute in item:
            key, value = attribute.split(": ", 1)  # Разделяем по ": " и берем 1 раз
            item_dict[key.strip()] = value.strip()  # Удаляем лишние пробелы
        result.append(item_dict)
    return result_dict


def append_zip(result_json, name, description, price):
    """Создает JSON список с собранными данными"""
    for nm, desc, pr in zip(name, description, price):
        result_json.append({'Название': nm, **desc, 'Цена': pr})
    return result_json


def create_json(result_json, filename='res.json'):
    """Создает JSON файл с собранными данными"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)
        print(f'Файл {filename} успешно создан.')


# Пример использования
base_url = 'https://parsinger.ru/html/index2_page_1.html'
base = parsing(base_url)
urls = collect_url_list(base_url, base)
result = []
for link in urls:
    base = parsing(link)
    name_l, description_l, price_l = collect_info(base)
    description_l = parse_description(description_l)
    append_zip(result, name_l, description_l, price_l)

create_json(result)
