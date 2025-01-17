# https://stepik.org/lesson/732069/step/3?unit=733602

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
    browser.get('https://parsinger.ru/infiniti_scroll_2/')

    unique_numbers = set()  # Используем множество для хранения уникальных чисел
    sum_num = 0

    scroll_element = browser.find_element(By.ID, 'scroll-container')

    while True:
        actions = ActionChains(browser)
        actions.click(scroll_element).key_down(Keys.PAGE_DOWN).perform()

        # Ждем, чтобы дать странице время на подгрузку новых элементов
        time.sleep(1)

        nums_elements = scroll_element.find_elements(By.TAG_NAME, 'p')

        new_elements = False

        for i in nums_elements:
            num = i.text.strip()
            if num.isdigit() and num not in unique_numbers:  # Проверка на уникальность и числовое значение
                unique_numbers.add(num)  # Добавляем новое число в множество
                sum_num += int(num)  # Сразу добавляем к общей сумме
                new_elements = True

        # Если новые элементы не были добавлены, выходим из цикла
        if not new_elements:
            print("Больше нет новых элементов для добавления.")
            print("Сумма числовых значений:", sum_num)
            break
