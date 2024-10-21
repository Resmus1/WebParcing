# Собрать данные с карточки и ссылку и сохранить в json
# Упустил указание категории, но немного надоело возиться поэтому оставлю как есть)

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json


def get_soup(url):
    """Получает и парсит страницу по указанному URL"""
    try:
        headers = {'User-Agent': UserAgent().random}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Проверка на успешный ответ. Выдаст ошибку если страница 404 и вернет None
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, 'lxml')
    except requests.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
        return None


def collect_page_list(home_url, soup):
    """Собирает список страниц в категории для парсинга"""
    url_list = []
    nav_menu = soup.find('div', class_='pagen')
    if nav_menu:
        for link in nav_menu.find_all('a', href=True):  # Поиск только ссылок с переходом на другой url.
            url_list.append(home_url.split('index')[0] + link['href'])
    return url_list


def collect_item_list(base_url, url_list):
    """Собирает весь список ссылок с товарами для парсинга"""
    item_list = []
    for url in url_list:
        soup = get_soup(url)
        links = soup.find('div', class_='item_card')
        if links:
            for item in links.find_all('a', string='Подробнее'):  # Поиск по тэгу p
                item_list.append(base_url.split('index')[0] + item['href'])
    return item_list


def collect_info(items):
    """Собирает данные с карточек и делает список"""
    item_desc_list = []
    for url in items:
        soup = get_soup(url)
        options = soup.find_all('div', class_='description')
        for item in options:
            name = item.find(id='p_header').get_text(strip=True)
            article = item.find(class_='article').get_text(strip=True).split(': ')[1]

            ext_desc = item.find('ul', id='description')
            description = {element['id']: element.get_text(strip=True).split(': ')[1]
                           for element in ext_desc.find_all('li')}

            count = item.find(id='in_stock').get_text(strip=True).split(': ')[1]
            price = item.find(id='price').get_text(strip=True)
            old_price = item.find(id='old_price').get_text(strip=True)
            link = url
            item_desc_list.append({'name': name, 'article': article, 'description': description, 'count': count,
                                   'price': price, 'old_price': old_price, 'link': link})
    return item_desc_list


def create_json(item_list, filename='res.json'):
    """Создает JSON файл с собранными данными"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(item_list, file, indent=4, ensure_ascii=False)
        print(f'Файл {filename} успешно создан.')
    except IOError as e:
        print(f"Ошибка при сохранении файла {filename}: {e}")


# Основной блок кода
def main():
    base_url = 'https://parsinger.ru/html/index5_page_1.html'
    main_page = get_soup(base_url)
    if not main_page:
        return
    pages = collect_page_list(base_url, main_page)
    items = collect_item_list(base_url, pages)
    items_desc_list = collect_info(items)
    create_json(items_desc_list)


if __name__ == '__main__':
    main()
