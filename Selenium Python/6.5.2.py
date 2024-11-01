# https://stepik.org/lesson/732065/step/1?unit=733598

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Настройки для браузера Chrome
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless=new')  # Запускаем браузер в фоновом режиме (без GUI)

# Используем контекстный менеджер для открытия браузера
with webdriver.Chrome(options=options_chrome) as browser:
    # Переходим на целевую страницу
    browser.get('https://parsinger.ru/infiniti_scroll_1/')

    sum_num = 0
    unique_numbers = set()  # Для хранения уникальных чисел

    scroll_element = browser.find_element(By.ID, 'scroll-container')

    while True:
        actions = ActionChains(browser)
        actions.click(scroll_element).key_down(Keys.PAGE_DOWN).perform()

        # Ждем, чтобы дать странице время на подгруздку новых элементов
        time.sleep(1)

        nums_elements = scroll_element.find_elements(By.TAG_NAME, 'span')

        for i in nums_elements:
            num = i.text.strip()
            if num.isdigit() and num not in unique_numbers:  # Проверка на уникальность
                sum_num += int(num)
                unique_numbers.add(num)  # Добавление уникального числа в множество

        # Проверяем, достигнут ли элемент с классом last-of-list
        try:
            last_of_list_element = scroll_element.find_element(By.CLASS_NAME, 'last-of-list')
            if last_of_list_element.is_displayed():  # Если элемент виден, выходим из цикла
                print("Достигнут элемент 'last-of-list'. Завершение сбора данных.")
                break
        except Exception:
            pass  # Если элемент не найден, продолжаем

    print("Сумма числовых значений:", sum_num)
