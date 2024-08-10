# Парсер для Авито с созданием таблицы
# Добавить изменение + отображение в терминале если произошли изменния цены
# Добавить чтение нескольких страниц
import csv
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Заранее подготовленный список десктопные User-Agent
desktop_user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
]


def initialize_browser():
    """Возвращаем откорректированную опцию веб драйвера"""
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={random.choice(desktop_user_agents)}')
    return webdriver.Chrome(options=options)


def read_file(file_path, mode='r', encoding='utf-8'):
    """Чтение файла и возврат содержимого в виде списка строк"""
    try:
        with open(file_path, mode, encoding=encoding) as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []


def write_file(file_path, data, mode='a', encoding='utf-8'):
    """Запись данных в файл"""
    with open(file_path, mode, encoding=encoding) as file:
        for line in data:
            file.write(line + '\n')


def read_csv(file_path, delimiter=';'):
    """Чтение CSV файла и возврат данных в виде множества"""
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file, delimiter=delimiter)
            next(reader)  # Пропустить заголовок
            return set(row[-1] for row in reader)
    except FileNotFoundError:
        return set()


def write_csv(file_path, data, headers=None, delimiter=';'):
    """Запись данных в CSV файл"""
    with open(file_path, 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=delimiter)
        if headers:
            writer.writerow(headers)
        writer.writerows(data)


def fetch_links(browser, url):
    """Извлечение новых ссылок с сайта"""
    browser.get(url)
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[itemprop="url"][data-marker="item-title"]'))
        )
        return [ad.get_attribute('href') for ad in
                browser.find_elements(By.CSS_SELECTOR, 'a[itemprop="url"][data-marker="item-title"]')]
    except TimeoutException:
        browser.save_screenshot('error_screenshot.png')
        return []


def fetch_data(browser, link, number):
    """Извлечение данных с одной страницы"""
    browser.get(link)
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'h1[itemprop="name"]'))
    )
    try:
        name = browser.find_element(By.CSS_SELECTOR, 'h1[itemprop="name"]').text.replace(',', '')
    except NoSuchElementException:
        name = 'Не указано'
    try:
        price = browser.find_element(By.CSS_SELECTOR, 'span[content]').get_attribute('content')
    except NoSuchElementException:
        price = 'Нет'

    params = browser.find_elements(By.CSS_SELECTOR, 'li[class="params-paramsList__item-_2Y2O"]')

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

    for param in params:
        param_text = param.text
        if ': ' in param_text:
            key, value = param_text.split(': ', 1)
            value = value.replace(',', '')
            if key in param_mapping:
                param_list[param_mapping[key]] = value
    return param_list


def main():
    start_time = time.time()

    links_file = 'links.txt'
    csv_file = 'avito.csv'
    url = 'https://www.avito.ru/omsk/noutbuki?cd=1&p=1&s=104'

    existing_links = read_file(links_file)
    existing_csv_links = read_csv(csv_file)

    with initialize_browser() as browser:
        new_links = fetch_links(browser, url)
        new_links = [link for link in new_links if link not in existing_links]

    write_file(links_file, new_links)
    existing_links.extend(new_links)

    headers = [
        '№', 'Состояние', 'Наименование', 'Цена', 'Производитель', 'Модель', 'Процессор', 'Видеокарта',
        'Объем видеопамяти', 'ОЗУ', 'Диагональ', 'Диск', 'Объем диска', 'Код конфигурации', 'Ссылка'
    ]
    write_csv(csv_file, [], headers=headers)

    number = 0
    try:
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file, delimiter=';')
            number = sum(1 for row in reader)  # Получаем количество строк
    except FileNotFoundError:
        pass

    with initialize_browser() as browser:
        data_to_write = []
        for link in existing_links:
            if link in existing_csv_links:
                continue

            number += 1
            try:
                param_list = fetch_data(browser, link, number)
                data_to_write.append(param_list)
            except (TimeoutException, NoSuchElementException) as e:
                print(f'Ошибка при обработке ссылки {link}: {e}')
                browser.save_screenshot(f'error_screenshot_{number}.png')
            time.sleep(random.uniform(5, 15))

    write_csv(csv_file, data_to_write)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Сбор данных завершен.", f"Время выполнения скрипта: {elapsed_time:.2f} секунд", sep='\n')


if __name__ == "__main__":
    main()
