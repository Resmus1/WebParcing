# Собрать данные со всех 5 категорий на сайте.
# (Позволил для автоматизации вписать русские ключи,
# но при желании и необходимости можно поставить модуль или написать словарь для преобразования текста.)

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json


def get_soup(url):
    """Получает и парсит страницу по указанному URL"""
    try:
        headers = {'User-Agent': UserAgent().random}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Проверка на успешный ответ
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, 'lxml')
    except requests.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
        return None


def collect_url_list(base_url, soup):
    """Собирает список ссылок для парсинга"""
    url_list = []
    nav_menu = soup.find('div', class_='nav_menu')
    if nav_menu:
        for link in nav_menu.find_all('a', href=True):
            url_list.append(base_url.split('index')[0] + link['href'])
    return url_list


def collect_info(soup):
    """Собирает данные с карточек"""
    names = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    descriptions = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
    prices = [x.text.strip() for x in soup.find_all('p', class_='price')]
    return names, descriptions, prices


def parse_description(description):
    """Преобразует данные из карточек в словарь"""
    result_dict = []
    for item in description:
        item_dict = {key.strip(): value.strip() for key, value in
                     (attr.split(": ", 1) for attr in item if ": " in attr)}
        result_dict.append(item_dict)
    return result_dict


def append_zip(result_json, names, descriptions, prices):
    """Добавляет данные в JSON список"""
    for name, desc, price in zip(names, descriptions, prices):
        result_json.append({'Название': name, **desc, 'Цена': price})


def create_json(result_json, filename='res.json'):
    """Создает JSON файл с собранными данными"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(result_json, file, indent=4, ensure_ascii=False)
        print(f'Файл {filename} успешно создан.')
    except IOError as e:
        print(f"Ошибка при сохранении файла {filename}: {e}")


# Основной блок кода
def main():
    base_url = 'https://parsinger.ru/html/index2_page_1.html'
    main_page = get_soup(base_url)
    if not main_page:
        return

    urls = collect_url_list(base_url, main_page)
    if not urls:
        print("Ссылки не найдены.")
        return

    result = []
    for link in urls:
        page_soup = get_soup(link)
        if page_soup:
            names, descriptions, prices = collect_info(page_soup)
            parsed_descriptions = parse_description(descriptions)
            append_zip(result, names, parsed_descriptions, prices)

    create_json(result)


if __name__ == '__main__':
    main()
