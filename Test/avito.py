# Парсер по Авито, парсит по готовому поиску

# Разбраться с IP при каких случаях происходит блок
# Перевести время в часы и минуты вместо секунд
# Проблемы с IP после нескольких обновлений могут пропадать
# Добавлена на 404 но нужно проверять сработает ли так или только при ошибки

import csv
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException

# Заранее подготовленный список десктопные User-Agent
desktop_user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 "
    "Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 "
    "Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 "
    "Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 "
    "Safari/537.36"
]

name_headers = [
    '№', 'Заголовок', 'Цена', 'Производитель', 'Модель', 'Процессор', 'Видеокарта', 'ОВУ', 'ОЗУ',
    'Диаг.', 'Диск', 'ПЗУ', 'Код конфигурации', 'Состояние', 'Описание', 'Контактное лицо', 'Тип продавца', 'Адрес',
    'Ссылка на объявление',
]


def initialize_browser():
    """Возвращаем откорректированную опцию веб драйвера"""
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={random.choice(desktop_user_agents)}')
    prefs = {"profile.managed_default_content_settings.images": 2}  # Отключение загрузки изображений
    options.add_experimental_option("prefs", prefs)
    # options.add_argument('--headless')  # Запуск браузера в режиме headless
    options.add_argument('--disable-gpu')  # Отключение GPU
    options.add_argument('--no-sandbox')  # Отключение песочницы
    options.add_argument('--disable-dev-shm-usage')  # Отключение использования /dev/shm
    options.add_argument('--window-size=800,800')  # Размер Окна
    options.add_argument('--disable-blink-features=AutomationControlled')  # Отключение уведомления о том что это робот

    # Установка прокси
    # options.add_argument('--proxy-server=http://your_proxy:port')

    try:
        print("Инициализация браузера с указанными параметрами:")
        print(f"User-Agent: {random.choice(desktop_user_agents)}")
        print(f"Options: {options.arguments}")
        browser = webdriver.Chrome(options=options)
        print("Браузер успешно инициализирован.")
        return browser
    except Exception as e:
        print(f'Ошибка инициализации браузера: {e}')
        return None


def read_file(file_path, mode='r', encoding='utf-8'):
    """
    Чтение файла и возврат содержимого в виде списка строк.

    :param file_path: Путь к файлу.
    :param mode: Режим открытия файла (по умолчанию 'r').
    :param encoding: Кодировка файла (по умолчанию 'utf-8').
    :return: Список строк из файла.
    """
    try:
        with open(file_path, mode, encoding=encoding) as file:
            print('Открытие файла со списком.')
            return [line.strip() for line in file]
    except FileNotFoundError:
        print('Файл не найден')
        return []


def add_new_elements(file_path, new_elements, existing_elements, encoding='utf-8'):
    """
    Добавление новых элементов в файл, если их еще нет в списке,
    и обновление списка существующих элементов.

    :param file_path: Путь к файлу.
    :param new_elements: Список новых элементов для добавления.
    :param existing_elements: Список существующих элементов.
    :param encoding: Кодировка файла (по умолчанию 'utf-8').
    :return: Обновленный список существующих элементов.
    """
    with open(file_path, 'a', encoding=encoding) as file:
        for element in new_elements:
            if element not in existing_elements:
                file.write(element + '\n')
                existing_elements.append(element)
    return existing_elements


def rw_csv(file_path, delimiter=';', headers=None):
    """
    Чтение CSV файла и возврат данных в виде множества.
    Если файл не найден, создать новый CSV файл с заголовками.

    :param file_path: Путь к файлу CSV.
    :param delimiter: Разделитель в CSV файле.
    :param headers: Список заголовков для нового файла, если оригинал не найден.
    :return: Множество ссылок из последнего столбца.
    """
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file, delimiter=delimiter)
            next(reader)  # Пропустить заголовок
            print('Открытие CSV файла.')
            return set(row[-1] for row in reader)
    except FileNotFoundError:
        print('Файл CSV не найден')
        if headers is not None:
            with open(file_path, 'w', encoding='utf-8-sig', newline='') as file:
                writer = csv.writer(file, delimiter=delimiter)
                writer.writerow(headers)
            print(f"CSV файл '{file_path}' успешно создан")
        return set()


def fetch_link_data(browser, link, existing_links):
    """
    Извлечение ссылок со страницы

    :param browser: Экземпляр веб-драйвера.
    :param link: Ссылка на страницу для парсинга.
    :param existing_links: Множество уже существующих ссылок.
    :return: Список новых ссылок.
    """
    browser.get(link)
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[itemprop="url"][data-marker="item-title"]'))
        )
        ads_elements = browser.find_elements(By.CSS_SELECTOR, 'a[itemprop="url"][data-marker="item-title"]')
        new_links = [ad.get_attribute('href') for ad in ads_elements if ad.get_attribute('href') not in existing_links]
        time.sleep(random.uniform(5, 15))
        return new_links
    except TimeoutException:
        browser.save_screenshot('error_screenshot.png')
        print(f'Ошибка ожидания, скриншот сохранен')  # СОЗДАТЬ КАКОЕТО ИМЯ А ЛУЧШЕ ССЫЛКУ ПОДПИСЬ К СКРИНШОТУ!
        return []


def new_link(browser, existing_links):
    """Обработка новых ссылок добавление в список

    :param browser: Экземпляр веб-драйвера.
    :param existing_links: Множество уже существующих ссылок.
    :return: Список новых ссылок."""
    all_new_links = []
    for i in range(1, 70):
        page_links = fetch_link_data(browser, f'https://www.avito.ru/omsk/noutbuki?cd=1&p={i}&s=104',
                                     existing_links)
        if page_links:
            all_new_links.extend(page_links)
            print(f'Найдено {len(all_new_links)} новых ссылок')
        else:
            print(f'Поиск завершен, найдено {len(all_new_links)} новых ссылок')
            break
    return all_new_links


def process_links(browser, links, existing_csv_links, csv_file):
    """
    Обработка списка ссылок и запись данных в CSV файл.

    :param browser: Инициализированный веб-драйвер.
    :param links: Список ссылок для обработки.
    :param existing_csv_links: Список уже существующих ссылок в CSV файле.
    :param csv_file: Путь к CSV файлу.
    """
    try:
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader, None)  # Пропускаем заголовок
            count_row = len(list(reader))  # Получаем количество строк
    except FileNotFoundError:
        print('CSV файл пуст')
        count_row = 0

    with open(csv_file, 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')

        count_links = len(links) - len(existing_csv_links)
        for link in links:
            link = link.strip()  # Удаление пробелов по краям
            if link in existing_csv_links:
                continue
            print(f'Осталось ссылок {count_links}')
            count_links -= 1
            count_row += 1
            print(f'Обработка элемента № {count_row} с ссылкой: {link}')

            try:
                browser.get(link)
                # Ожидание, пока элементы будут видимы на новой странице
                WebDriverWait(browser, 20).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'h1[itemprop="name"]'))
                )

                # Проверка на 404
                if "К сожалению, это объявление больше не доступно" in browser.page_source:
                    print(f'Ссылка {link} недоступна (404). Удаление ссылки.')
                    links.remove(link)
                    continue

                # Обработка имени
                try:
                    name = browser.find_element(By.CSS_SELECTOR, 'h1[itemprop="name"]').text.replace(',', '')
                except NoSuchElementException:
                    name = 'Не указано'

                # Обработка цены
                try:
                    price = browser.find_element(By.CSS_SELECTOR, 'span[content]').get_attribute('content')
                except NoSuchElementException:
                    price = 'Нет'

                # Обработка параметров
                params = browser.find_elements(By.CSS_SELECTOR, 'li[class="params-paramsList__item-_2Y2O"]')

                # Обработка описания
                try:
                    description_element = browser.find_element(By.CSS_SELECTOR,
                                                               'div[data-marker="item-view/item-description"] p')
                    description = description_element.text.replace(',', '')
                except NoSuchElementException:
                    description = 'Нет'

                # Обработка информации о продавце
                seller_info_elements = browser.find_elements(By.CSS_SELECTOR,
                                                             'div[class="style-seller-info-col-PETb_"]')

                # Инициализация переменных значениями по умолчанию
                seller = 'Нет'
                type_seller = 'Нет'

                for seller_info in seller_info_elements:
                    try:
                        seller = seller_info.find_element(By.CLASS_NAME, 'styles-module-size_ms-YUHT8').text
                        type_seller = seller_info.find_element(By.CSS_SELECTOR,
                                                               'div[data-marker="seller-info/label"]').text
                        break  # Выход из цикла, если элемент найден
                    except NoSuchElementException:
                        continue  # Переход к следующему элементу, если не найдено

                # Обработка адреса
                try:
                    ads_seller = browser.find_element(By.CSS_SELECTOR,
                                                      'span[class="style-item-address__string-wt61A"]').text.replace(
                        ',', '')
                except NoSuchElementException:
                    ads_seller = 'Нет'

                # Создаем список с нужным количеством элементов, заполняем его пустыми строками
                param_list = [count_row, name, price, 4, '', '', '', '', '', '', '', '', '', '', description, seller,
                              type_seller, ads_seller, link]
                param_mapping = {
                    'Производитель': 3,
                    'Модель': 4,
                    'Процессор': 5,
                    'Видеокарта': 6,
                    'Объем видеопамяти': 7,
                    'Оперативная память': 8,
                    'Диагональ': 9,
                    'Конфигурация накопителей': 10,
                    'Объем накопителей': 11,
                    'Код конфигурации': 12,
                    'Состояние': 13,
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

            except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
                if NoSuchElementException:
                    # Блокировка IP
                    if "Доступ ограничен: проблема с IP" in browser.page_source:
                        print('Блокировка IP')
                        exit()
                print(f'Ошибка при обработке ссылки {link}: {e}')
                # Можно сохранить скриншот страницы для анализа
                browser.save_screenshot(f'error_screenshot_{count_row}.png')

            # Случайная задержка между запросами (например, от 5 до 15 секунд)
            time.sleep(random.uniform(5, 15))


def main():
    start_time = time.time()  # Зафиксировать время начала выполнения скрипта
    list_file = 'links.txt'
    csv_file = 'avito.csv'

    # Считать уже существующие ссылки из файла
    existing_links = read_file(list_file)
    # Прочитать CSV файл и создать его, если он не существует
    existing_csv_links = rw_csv('avito.csv', headers=name_headers)

    browser = initialize_browser()
    if not browser:
        print("Ошибка инициализации браузера. Завершение работы.")
        return
    # Поиск ссылок на странице
    all_new_links = new_link(browser, existing_links)
    # Добавление новых элементов и изменение списка
    add_new_elements(list_file, all_new_links, existing_links)
    # Обработка ссылок
    process_links(browser, existing_links, existing_csv_links, csv_file)

    # Зафиксировать время окончания выполнения скрипта
    end_time = time.time()
    # Вычислить разницу во времени и вывести
    elapsed_time = end_time - start_time
    print("Сбор данных завершен.", f"Время выполнения скрипта: {elapsed_time:.2f} секунд", sep='\n')


if __name__ == "__main__":
    main()
