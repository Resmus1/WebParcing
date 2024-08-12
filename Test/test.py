import csv
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

desktop_user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
]

name_headers = [
    '№', 'Состояние', 'Наименование', 'Цена', 'Производитель', 'Модель', 'Процессор', 'Видеокарта',
    'Объем видеопамяти', 'ОЗУ', 'Диагональ', 'Диск', 'Объем диска', 'Код конфигурации', 'Ссылка'
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

def new_link(browser, existing_links):
    all_new_links = []
    for i in range(1, 70):
        page_links = fetch_link_data(browser, f'https://www.avito.ru/omsk/noutbuki?cd=1&p={i}&s=104', existing_links)
        if page_links:
            all_new_links.extend(page_links)
            print(f'Найдено {len(all_new_links)} новых ссылок')
        else:
            print(f'Поиск завершен, найдено {len(all_new_links)} новых ссылок')
            break
    return all_new_links

def fetch_link_data(browser, link, existing_links):
    """
    Извлечение ссылок со страницы
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
        print(f'Ошибка ожидания, скриншот сохранен')
        return []

def process_links(browser, links, existing_csv_links, csv_file):
    """
    Обработка списка ссылок и запись данных в CSV файл.
    """
    try:
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader, None)  # Пропускаем заголовок
            count_row = sum(1 for row in reader)  # Получаем количество строк
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
                    continue

                # Обработка имени
                try:
                    name = browser.find_element(By.CSS_SELECTOR, 'h1[itemprop="name"]').text
                except NoSuchElementException:
                    name = 'Не указано'

                # Обработка цены
                try:
                    price = browser.find_element(By.CSS_SELECTOR, 'span[itemprop="price"]').get_attribute("content")
                except NoSuchElementException:
                    price = 'Не указана'

                # Обработка остальных элементов
                try:
                    characteristics = browser.find_elements(By.CSS_SELECTOR, 'li[data-marker="item-params-list-item"]')
                    characteristics = [item.text.split(': ') for item in characteristics]
                    characteristics_dict = {key: value for key, value in characteristics}

                    manufacturer = characteristics_dict.get('Производитель', 'Не указано')
                    model = characteristics_dict.get('Модель', 'Не указано')
                    processor = characteristics_dict.get('Процессор', 'Не указано')
                    graphics_card = characteristics_dict.get('Видеокарта', 'Не указано')
                    video_memory = characteristics_dict.get('Объем видеопамяти', 'Не указано')
                    ram = characteristics_dict.get('Оперативная память', 'Не указано')
                    screen_size = characteristics_dict.get('Диагональ экрана', 'Не указано')
                    drive_type = characteristics_dict.get('Тип жесткого диска', 'Не указано')
                    drive_capacity = characteristics_dict.get('Объем жесткого диска', 'Не указано')
                    configuration_code = characteristics_dict.get('Код конфигурации', 'Не указано')

                except NoSuchElementException:
                    manufacturer = model = processor = graphics_card = video_memory = ram = screen_size = drive_type = drive_capacity = configuration_code = 'Не указано'

                status = "Б/у" if "Б/у" in name else "Новый"

                # Запись данных в CSV
                writer.writerow([
                    count_row, status, name, price, manufacturer, model, processor, graphics_card, video_memory, ram,
                    screen_size, drive_type, drive_capacity, configuration_code, link
                ])
                time.sleep(random.uniform(5, 15))  # Пауза перед следующей итерацией
            except TimeoutException:
                print(f'Ошибка при обработке ссылки {link}')
                continue

def main():
    list_file = 'List.txt'
    csv_file = 'LinkNotebook.csv'

    existing_links = read_file(list_file)
    existing_csv_links = rw_csv(csv_file, headers=name_headers)

    browser = initialize_browser()
    if not browser:
        print("Ошибка инициализации браузера. Завершение работы.")
        return

    try:
        new_links = new_link(browser, existing_csv_links)
        if new_links:
            existing_links = add_new_elements(list_file, new_links, existing_links)
            process_links(browser, new_links, existing_csv_links, csv_file)
        else:
            print('Нет новых ссылок для обработки.')
    finally:
        browser.quit()
        print("Браузер закрыт.")

if __name__ == '__main__':
    main()