#  https://stepik.org/lesson/732083/step/7?unit=733616

# Импортируем необходимые библиотеки для работы с Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Настройки для запуска браузера в headless-режиме
options = Options()
options.add_argument('--headless=new')  # Запуск в безголовом режиме (без графического интерфейса)

# Список для хранения текста кнопок
result = []

if __name__ == '__main__':
    try:
        # Открытие браузера и загрузка страницы
        with webdriver.Chrome(options=options) as browser:
            browser.get('https://parsinger.ru/selenium/5.9/5/index.html')

            # Находим все кнопки с классом 'box_button'
            button = browser.find_elements(By.CLASS_NAME, 'box_button')

            for i in range(len(button)):
                button[i].click()  # Клик по кнопке

                # Закрываем рекламное окно
                browser.find_element(By.ID, 'close_ad').click()

                # Ожидаем, пока рекламное окно исчезнет
                WebDriverWait(browser, 30).until(EC.invisibility_of_element((By.ID, 'ad_window')))

                # Формируем локатор для текущей кнопки
                button_locator = f'.box_button:nth-of-type({i + 1})'

                # Ожидаем появления текста в кнопке
                WebDriverWait(browser, 30).until(lambda driver: len(driver.find_element(By.CSS_SELECTOR, button_locator).text) > 0)

                # Добавляем текст кнопки в результат
                result.append(button[i].text)

            # Печать всех текстов кнопок через дефис
            print('-'.join(result))

    except Exception as e:
        print(f"Alert: {e}")  # Вывод ошибки, если что-то пошло не так
