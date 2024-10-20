# Собрать все данные с карточек в файл json.
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json


def parsing(url):
    """Парсит указанную страницу по правилам"""
    headers = {'User-Agent': UserAgent().random}
    try:
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        if response.status_code != 200:
            raise Exception(f"Ошибка при запросе: {response.status_code}")
        soup = BeautifulSoup(response.text, 'lxml')
        return soup
    except requests.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return None


def collect_info(soup):
    """Собирает все данные с карточек"""
    name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
    price = [x.text for x in soup.find_all('p', class_='price')]

    # Проверка на случай отсутствия данных
    if not (name and description and price):
        print("Данные не найдены.")
        return [], [], []

    return name, description, price


def parse_description(description):
    """Извлекает данные из описания карточки"""
    try:
        brand = description[0].split(': ')[1].strip()
        type = description[1].split(':')[1].strip()
        connect = description[2].split(': ')[1].strip()
        game = description[3].split(': ')[1].strip()
        return brand, type, connect, game
    except (IndexError, ValueError):
        return None, None, None, None  # Если вдруг чего-то не хватает


def create_zip(name, description, price):
    """Создает JSON список с собранными данными"""
    result_json = []
    for desc, pr, nm in zip(description, price, name):
        brand, type, connect, game = parse_description(desc)
        if None not in (brand, type, connect, game):  # Только если все данные корректны
            result_json.append({
                'name': nm,
                'brand': brand,
                'type': type,
                'connect': connect,
                'game': game,
                'price': pr,
            })
    return result_json


def create_json(result_json, filename='res.json'):
    """Создает JSON файл с собранными данными"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)
        print(f'Файл {filename} успешно создан.')


# Пример использования
url = 'https://parsinger.ru/html/index2_page_1.html'
soup = parsing(url)

if soup:
    list_name, list_description, list_price = collect_info(soup)
    result = create_zip(list_name, list_description, list_price)

    if result:
        create_json(result)
    else:
        print("Нет данных для записи.")
