# Напишите код который собирает данные в каждой категории каждой карточки всего их 160
import csv
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
# Убрать лишние категрии и все будет работатать корректнно, перед этим посмотреть res

def parsing(url):
    """Парсит страницу"""
    headers = {'User-Agent': UserAgent().random}
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


# Нужно сделать категории как ключи а страницы как данные!!!!!!!!!!!!
def collect_url(base_url, first_url):
    """Собирает все ссылки со всех категорий и преобразует в список"""
    soup = parsing(base_url.format(first_url))
    link_page = []
    category = soup.find(class_="nav_menu").find_all('a')
    for c in category:
        soup_category = parsing(base_url.format(c['href']))
        pages = soup_category.find(class_="pagen").find_all('a')
        for p in pages:
            soup_url_pages = parsing(base_url.format(p['href']))
            links = soup_url_pages.find_all('a', class_='name_item')
            for link in links:
                link_page.append(base_url.format(link['href']))
    return link_page


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
    first_link = 'index1_page_1.html'

    urls = collect_url(home, first_link)
    for item_url in urls:
        print('Done', item_url)
        item_in_url = parsing(item_url)
        item_data = parse_page(item_in_url, item_url)
        writer.writerow(item_data)
