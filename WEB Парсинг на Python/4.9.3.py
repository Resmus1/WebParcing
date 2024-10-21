# Собрать данные с карточки и ссылку и сохранить в json


import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json


def get_soup(url):
    """Получает и парсит страницу по указанному URL"""
    try:
        headers = {'User-Agent': UserAgent().random}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, 'lxml')
    except requests.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
        return None


def collect_page_list(home_url, soup):
    """Собирает список страниц в категории для парсинга"""
    url_list = set()  # Используем set для уникальности
    nav_menu = soup.find('div', class_='pagen')
    if nav_menu:
        for link in nav_menu.find_all('a', href=True):
            full_url = home_url.split('index')[0] + link['href']
            url_list.add(full_url)  # Добавляем уникальный URL
    return list(url_list)  # Преобразуем обратно в список


def collect_item_list(base_url, url_list):
    """Собирает весь список ссылок с товарами для парсинга"""
    item_list = set()  # Используем set для уникальности
    for url in url_list:
        soup = get_soup(url)
        if not soup:
            continue  # Пропускаем, если страница не была загружена
        links = soup.find('div', class_='item_card')
        if links:
            for item in links.find_all('a', string='Подробнее'):
                item_list.add(base_url.split('index')[0] + item['href'])  # Добавляем уникальный URL
    return list(item_list)  # Преобразуем обратно в список


def collect_info(items):
    """Собирает данные с карточек и делает список"""
    item_desc_list = []
    for url in items:
        soup = get_soup(url)
        if not soup:
            continue  # Пропускаем, если страница не была загружена
        descriptions = soup.find_all('div', class_='description')
        for item in descriptions:
            name = item.find(id='p_header')
            article = item.find(class_='article')
            ext_desc = item.find('ul', id='description')
            count = item.find(id='in_stock')
            price = item.find(id='price')
            old_price = item.find(id='old_price')

            # Проверка на существование элементов перед их использованием
            if name and article and ext_desc and count and price and old_price:
                description = {element['id']: element.get_text(strip=True).split(': ')[1]
                               for element in ext_desc.find_all('li')}
                item_desc_list.append({
                    'name': name.get_text(strip=True),
                    'article': article.get_text(strip=True).split(': ')[1],
                    'description': description,
                    'count': count.get_text(strip=True).split(': ')[1],
                    'price': price.get_text(strip=True),
                    'old_price': old_price.get_text(strip=True),
                    'link': url
                })
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
