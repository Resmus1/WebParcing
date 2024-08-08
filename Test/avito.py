# Парсер для Авито с созданием таблицы
# Добавить изменение + отображение в терминале если произошли изменния цены
# Уточнить подходит ли рандом от 5-15 сам рандом занял время
# Подумать добавлять ли инфо о продавце
# Почему-то сразу не пробегает по новым ссылкам, а лишь на следующий запуск, похоже не сохраняет или сохраняет после
# Создать FakeUSER
# Создать подсчет количества оставшихся ссылок, нужно счиать не новые ссылки, а то что насчитало количчество необработаных ссылок и уже по ним вести счет
# Также возникла ошибка, страница не догрузилась, нужно добавить правило повторной загрузки или еще чего
import csv
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Зафиксировать время начала выполнения скрипта
start_time = time.time()

links_file = 'links.txt'
csv_file = 'avito.csv'

# Считать уже существующие ссылки из файла
existing_links = []
try:
    with open(links_file, 'r', encoding='utf-8') as file:
        existing_links = [line.strip() for line in file]  # Сохраняем порядок
        print('Открытие файла со списком.')
except FileNotFoundError:
    print('Файл не обнаружен, создание списка ссылок')
    existing_links = []

# Считать уже существующие ссылки из CSV-файла
existing_csv_links = set()
try:
    with open(csv_file, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # Пропустить заголовок
        existing_csv_links.update(row[-1] for row in reader)
        print('Открытие CSV файла.')
except FileNotFoundError:
    print('Файл CSV не найден, создание CSV')
    existing_csv_links = set()

# Инициализация веб-драйвера
with webdriver.Chrome() as browser:
    url = 'https://www.avito.ru/omsk/noutbuki?cd=1&p=1&s=104'
    browser.get(url)

    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[itemprop="url"][data-marker="item-title"]'))
        )
        ads_elements = browser.find_elements(By.CSS_SELECTOR, 'a[itemprop="url"][data-marker="item-title"]')
        new_links = [ad.get_attribute('href') for ad in ads_elements if ad.get_attribute('href') not in existing_links]
        print(f'Найдено {len(new_links)} новых ссылок.')
    except TimeoutException as e:
        browser.save_screenshot('error_screenshot.png')
        print(f'Ошибка ожидания: {e}, скриншот сохранен')
        exit(1)

# Сохранение новых ссылок в файл и открытие нового файла
with open(links_file, 'a', encoding='utf-8') as file:
    for link in new_links:
        file.write(link + '\n')
with open(links_file, 'r', encoding='utf-8') as file:
    existing_links = [line.strip() for line in file]  # Сохраняем порядок
print('Новые ссылки сохранены в файл.')

# Проверка и запись заголовков, если необходимо
headers_written = False
try:
    with open(csv_file, 'r+', encoding='utf-8-sig', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        first_row = next(reader, None)
        if first_row != [
            '№', 'Состояние', 'Наименование', 'Цена', 'Производитель', 'Модель', 'Процессор', 'Видеокарта',
            'Объем видеопамяти', 'ОЗУ', 'Диагональ', 'Диск', 'Объем диска', 'Код конфигурации', 'Ссылка'
        ]:
            headers_written = True
        file.seek(0, 2)  # Переместить указатель в конец файла для записи новых данных
except FileNotFoundError:
    headers_written = True
# Запись заголовков в CSV
if headers_written:
    with open(csv_file, 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([
            '№', 'Состояние', 'Наименование', 'Цена', 'Производитель', 'Модель', 'Процессор', 'Видеокарта',
            'Объем видеопамяти', 'ОЗУ', 'Диагональ', 'Диск', 'Объем диска', 'Код конфигурации', 'Ссылка'
        ])

# Обработка новых ссылок
with webdriver.Chrome() as browser:
    number = 0
    try:
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file, delimiter=';')
            number = sum(1 for row in reader)  # Получаем количество строк
    except FileNotFoundError:
        print('CSV файл пуст')

    with open(csv_file, 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')

        for link in existing_links:
            link = link.strip()  # Удаление пробелов по краям
            if link in existing_csv_links:
                continue

            number += 1
            print(f'Обработка элемента № {number} с ссылкой: {link}')
            try:
                browser.get(link)

                # Ожидание, пока элементы будут видимы на новой странице
                WebDriverWait(browser, 20).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'h1[itemprop="name"]'))
                )
                # Обработка имени (try-except) добавлен на всякий случай!
                try:
                    name = browser.find_element(By.CSS_SELECTOR, 'h1[itemprop="name"]').text.replace(',', '')
                except NoSuchElementException:
                    name = 'Не указано'  # Или любое другое значение по умолчанию
                # Обработка цены
                try:
                    price = browser.find_element(By.CSS_SELECTOR, 'span[content]').get_attribute('content')
                except NoSuchElementException:
                    price = 'Нет'

                params = browser.find_elements(By.CSS_SELECTOR, 'li[class="params-paramsList__item-_2Y2O"]')

                # Создаем список с нужным количеством элементов, заполняем его пустыми строками
                param_list = [number, '', name, price, '', '', '', '', '', '', '', '', '', '', link]
                param_mapping = {
                    'Состояние': 1,
                    'Производитель': 4,
                    'Модель': 5,
                    'Процессор': 6,
                    'Видеокарта': 7,
                    'Объем видеопамяти': 8,
                    'Оперативная память': 9,
                    'Диагональ': 10,
                    'Конфигурация накопителей': 11,
                    'Объем накопителей': 12,
                    'Код конфигурации': 13,
                }

                # Заполнение параметров
                for param in params:
                    param_text = param.text
                    if ': ' in param_text:
                        key, value = param_text.split(': ', 1)
                        value = value.replace(',', '')
                        if key in param_mapping:
                            param_list[param_mapping[key]] = value
                print('Обработка элемента завершена.')

                # Запись данных в CSV
                writer.writerow(param_list)
                print('Запись данных завершена.')

            except (TimeoutException, NoSuchElementException) as e:
                print(f'Ошибка при обработке ссылки {link}: {e}')
                # Можно сохранить скриншот страницы для анализа
                browser.save_screenshot(f'error_screenshot_{number}.png')

            # Случайная задержка между запросами (например, от 5 до 15 секунд)
            time.sleep(random.uniform(5, 15))

# Зафиксировать время окончания выполнения скрипта
end_time = time.time()

# Вычислить разницу во времени и вывести
elapsed_time = end_time - start_time
print("Сбор данных завершен.", f"Время выполнения скрипта: {elapsed_time:.2f} секунд", sep='\n')
