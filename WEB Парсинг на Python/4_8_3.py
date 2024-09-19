# Напишите код, который собирает данные в категории каждой карточки всего их 32
import csv
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


def parsing(url):
    """Парсит страницу"""
    headers = {'User-Agent': UserAgent().random}
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def collect_url(soup):
    """Собирает все ссылки с категории"""
    all_link = []
    url_category = 'https://parsinger.ru/html/index1_page_{}.html'
    for i in range(1, len(soup.find(class_="pagen").find_all('a')) + 1):
        soup_url_category = parsing(url_category.format(i))
        links = soup_url_category.find_all('a', class_='name_item')
        for link in links:
            all_link.append(link['href'])
    return all_link


def parse_page(soup, i_link):
    """Парсит страницу товара"""
    list_param = [soup.find(id='p_header').text]  # Наименование товара
    list_item = soup.find_all('li')  # Список характеристик

    # Добавляем артикул в начало списка
    list_item.insert(0, soup.find(class_='article'))

    # Добавляем наличие на 9-ю позицию
    list_item.insert(9, soup.find(id="in_stock"))

    for item in list_item:
        # Разделяем только по первому двоеточию и сохраняем всё, что после двоеточия, как одно значение
        parsed_item = item.text.strip().split(':', 1)
        if len(parsed_item) > 1:
            list_param.append(parsed_item[1].strip())  # Добавляем значение характеристики

    # Добавляем цену и старую цену
    list_param.append(soup.find(id="price").text)
    list_param.append(soup.find(id="old_price").text)
    # Добавляем ссылку на товар
    list_param.append(i_link)

    return list_param


with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    # Настройки CSV writer: используем точку с запятой как разделитель и включаем кавычки для всех значений
    writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

    # Заголовок таблицы
    writer.writerow(
        ['Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип подключения', 'Технология экрана', 'Материал корпуса',
         'Материал браслета', 'Размер', 'Сайт производителя', 'Наличие', 'Цена', 'Старая цена',
         'Ссылка на карточку с товаром'])

    home = 'https://parsinger.ru/html/{}'

    base_url = parsing(home.format('index1_page_1.html'))
    urls = collect_url(base_url)
    for item_url in urls:
        item_link = home.format(item_url)
        item_in_url = parsing(item_link)
        item_data = parse_page(item_in_url, item_link)
        writer.writerow(item_data)
