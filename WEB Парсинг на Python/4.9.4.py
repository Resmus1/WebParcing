# Нужно собрать данные с карточек всех категорий

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json


def get_soup(url, headers):
    """Парсит страницу и возвращает объект BeautifulSoup."""
    try:
        # Выполняем GET-запрос к указанному URL с заголовками
        response = requests.get(url, headers=headers, timeout=10)
        # Проверяем, успешно ли выполнен запрос (статус код 200)
        response.raise_for_status()  # Если статус код не 200, будет вызвано исключение
        # Устанавливаем кодировку, чтобы текст был корректно прочитан
        response.encoding = 'utf-8'
        # Возвращаем объект BeautifulSoup для дальнейшего парсинга
        return BeautifulSoup(response.text, 'lxml')
    except requests.RequestException as e:
        # Обрабатываем исключения, связанные с запросами
        print(f"Ошибка при запросе к {url}: {e}")
        return None  # Возвращаем None, если произошла ошибка


def collect_category_dict(url, soup):
    """Собирает категории с использованием id внутреннего div в качестве ключа."""
    category_dict = {}
    # Ищем навигационное меню на странице
    nav_menu = soup.find('div', class_='nav_menu')
    if nav_menu:
        # Ищем все ссылки внутри навигационного меню
        for link in nav_menu.find_all('a', href=True):
            # Ищем тег <div> внутри ссылки и получаем его id
            div = link.find('div')
            if div and div.get('id'):  # Проверяем, что div существует и у него есть id
                link_id = div.get('id')  # Получаем значение id для использования в качестве ключа
                # Формируем полный URL, объединяя базовый URL и относительный путь из href
                full_url = url.split('index')[0] + link['href']
                # Добавляем пару ключ-значение в словарь: id div как ключ, полный URL как значение
                category_dict.update({link_id: full_url})
    return category_dict  # Возвращаем словарь с категориями и соответствующими ссылками


def collect_item_list(url, headers, soup):
    """Собирает список страниц в категории для парсинга."""
    # Получаем словарь категорий с помощью функции collect_category_dict
    category_dict = collect_category_dict(url, soup)
    for key_category, url_category in category_dict.items():
        item_set = set()  # Используем множество для хранения уникальных URL товаров
        # Парсим страницу категории
        soup = get_soup(url_category, headers)
        if not soup:  # Если не удалось получить страницу, переходим к следующей категории
            continue
        # Ищем контейнер с товарами
        items_url = soup.find('div', class_='item_card')
        if items_url:
            # Ищем все ссылки с текстом "Подробнее"
            for item in items_url.find_all('a', string='Подробнее'):
                # Формируем полный URL для товара и добавляем его в множество
                item_set.add(url.split('index')[0] + item['href'])
        # Обновляем словарь категорий, добавляя список ссылок на товары для каждой категории
        category_dict[key_category] = list(item_set)
    return category_dict  # Возвращаем обновленный словарь категорий с товарами


def collect_info(headers, category_dict):
    """Собирает данные с карточек товаров и формирует список с информацией о товарах."""
    item_desc_list = []  # Список для хранения информации о каждом товаре
    for key_category, urls_category in category_dict.items():
        # Перебираем все URL товаров в каждой категории
        for url in urls_category:
            # Парсим страницу товара
            soup = get_soup(url, headers)
            if not soup:  # Если не удалось получить страницу, переходим к следующему товару
                continue
            # Ищем все блоки с описанием товара
            descriptions = soup.find_all('div', class_='description')
            for item in descriptions:
                # Извлекаем данные по атрибутам товара
                category = key_category  # Категория берется из ключа словаря категорий
                name = item.find(id='p_header')  # Название товара
                article = item.find(class_='article')  # Артикул товара
                ext_desc = item.find('ul', id='description')  # Расширенное описание (список характеристик)
                count = item.find(id='in_stock')  # Количество на складе
                price = item.find(id='price')  # Цена товара
                old_price = item.find(id='old_price')  # Старая цена товара

                # Проверяем, что все необходимые элементы существуют
                if name and article and ext_desc and count and price and old_price:
                    # Формируем словарь с расширенным описанием (характеристиками) товара
                    description = {element['id']: element.get_text(strip=True).split(': ')[1]
                                   for element in ext_desc.find_all('li')}
                    # Добавляем информацию о товаре в список
                    item_desc_list.append({
                        'categories': category,
                        'name': name.get_text(strip=True),
                        'article': article.get_text(strip=True).split(': ')[1],
                        'description': description,
                        'count': count.get_text(strip=True).split(': ')[1],
                        'price': price.get_text(strip=True),
                        'old_price': old_price.get_text(strip=True),
                        'link': url
                    })
    return item_desc_list  # Возвращаем список с описаниями товаров


def create_json(item_list, filename='res.json'):
    """Создает JSON файл с собранными данными."""
    try:
        # Записываем данные в файл JSON
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(item_list, file, indent=4, ensure_ascii=False)
        print(f'Файл {filename} успешно создан.')  # Сообщаем об успешном создании файла
    except IOError as e:
        # Обрабатываем ошибки, которые могут возникнуть при записи в файл
        print(f"Ошибка при сохранении файла {filename}: {e}")


# Основной блок кода
def main():
    url = 'https://parsinger.ru/html/index1_page_1.html'  # Стартовая страница для парсинга
    headers = {'User-Agent': UserAgent().random}  # Используем случайный User-Agent для обхода блокировок
    soup = get_soup(url, headers)  # Парсим стартовую страницу
    if soup:  # Проверяем, удалось ли получить объект BeautifulSoup
        category_dict = collect_item_list(url, headers, soup)  # Собираем список категорий и товаров
        item_list = collect_info(headers, category_dict)  # Собираем данные о каждом товаре
        create_json(item_list)  # Записываем собранные данные в JSON файл
    else:
        print("Не удалось получить исходный soup для URL.")  # Сообщаем о невозможности продолжить парсинг


# Запуск основного блока, если файл выполняется как самостоятельный скрипт
if __name__ == '__main__':
    main()
