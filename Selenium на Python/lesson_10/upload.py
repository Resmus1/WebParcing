#  https://stepik.org/lesson/1164775/step/1?unit=1177119

import os  # Импортируем модуль для работы с файловой системой
import time  # Импортируем модуль для работы с задержками

from selenium import webdriver  # Импортируем Selenium для автоматизации браузера

# Настройка параметров браузера Chrome
chrome_option = webdriver.ChromeOptions()
chrome_option.page_load_strategy = 'eager'  # Устанавливаем стратегию загрузки страницы: "eager" (основное содержимое загружается до начала работы кода)
chrome_option.add_argument('--headless=new')  # Запускаем браузер в headless-режиме (без графического интерфейса)

# Запуск браузера и выполнение действий
with webdriver.Chrome() as browser:
    browser.get('https://the-internet.herokuapp.com/upload')  # Переходим на страницу с формой загрузки файла

    # Находим элемент <input> для загрузки файла с атрибутом type='file'
    upload_file = browser.find_element('xpath', "//input[@type='file']")

    # Передаем полный путь к файлу, который хотим загрузить
    # os.path.abspath('downloads/Test.jpg') формирует абсолютный путь для указанного файла
    upload_file.send_keys(os.path.abspath('downloads/Test.jpg'))

    # Ожидаем 3 секунды, чтобы убедиться, что загрузка завершилась (можно заменить на более надежный способ)
    time.sleep(3)
