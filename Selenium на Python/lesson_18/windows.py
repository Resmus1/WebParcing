#  https://stepik.org/lesson/1164750/step/1?unit=1177094
import time  # Импортируем модуль для работы со временем

from selenium import webdriver  # Импортируем модуль для работы с браузером через Selenium

# Настраиваем параметры браузера
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")  # Указываем размер окна браузера (ширина x высота)

# Создаем экземпляр браузера с заданными параметрами
with webdriver.Chrome(options=chrome_options) as browser:
    try:
        # Открываем первую страницу (Google)
        browser.get('https://www.google.com/')
        time.sleep(3)  # Делаем паузу в 3 секунды, чтобы страница успела загрузиться

        # Открываем новую вкладку
        browser.switch_to.new_window("tab")  # Создаем новую вкладку
        browser.get("https://yandex.kz/")  # Загружаем страницу Яндекса в новой вкладке
        time.sleep(3)  # Ждем 3 секунды

        # Получаем список всех открытых окон/вкладок
        windows = browser.window_handles

        # Переключаемся обратно на первую вкладку (Google)
        browser.switch_to.window(windows[0])  # Переключаемся на первое окно (по индексу 0)
        time.sleep(3)  # Ждем 3 секунды

    except Exception as e:
        # Если возникает ошибка, выводим сообщение об ошибке
        print(f"ERROR: {e}")
