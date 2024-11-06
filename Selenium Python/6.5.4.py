# https://stepik.org/lesson/732069/step/4?unit=733602

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
    browser.get('https://parsinger.ru/infiniti_scroll_3/')

    # Переменная для хранения общей суммы числовых значений
    sum_num = 0

    # Проходим по каждому контейнеру с числами (от scroll-container_1 до scroll-container_5)
    for i in range(1, 6):
        # Находим элемент контейнера по его ID
        scroll_element = browser.find_element(By.ID, f'scroll-container_{i}')

        # Инициализируем переменную для отслеживания количества найденных элементов
        prev_length = 0

        # Бесконечный цикл для прокрутки контейнера и подгрузки новых элементов
        while True:
            # Создаем действие прокрутки вниз для элемента контейнера
            actions = ActionChains(browser)
            actions.click(scroll_element).key_down(Keys.PAGE_DOWN).perform()

            # Ждем, чтобы дать странице время на подгрузку новых элементов
            time.sleep(1)

            # Находим все элементы <span> в контейнере
            nums_elements = scroll_element.find_elements(By.TAG_NAME, 'span')

            # Считаем текущее количество элементов
            curr_length = len(nums_elements)

            # Проверяем, изменилось ли количество элементов
            if curr_length == prev_length:
                # Если новых элементов нет, суммируем все найденные значения
                for i_num in nums_elements:
                    # Получаем текст из <span> элемента и преобразуем его в число
                    num = i_num.text.strip()
                    sum_num += int(num)
                # Прерываем цикл, так как больше нет новых элементов
                break

            # Обновляем prev_length для следующей итерации
            prev_length = curr_length

        # Выводим сумму чисел после обработки текущего контейнера
        print("Сумма числовых значений:", sum_num)
