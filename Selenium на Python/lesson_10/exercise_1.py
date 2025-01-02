#  https://stepik.org/lesson/1164777/step/1?unit=1177120

import os  # Импортируем модуль для работы с файловой системой
import time  # Импортируем модуль для работы с задержками

from selenium import webdriver  # Импортируем Selenium для автоматизации браузера

# Запуск браузера Chrome
with webdriver.Chrome() as browser:
    # Открываем веб-страницу с возможностью загрузки/выгрузки файлов
    browser.get('https://demoqa.com/upload-download')

    # Находим элемент <input> для загрузки файла с атрибутом type='file'
    upload_button = browser.find_element('xpath', "//input[@type='file']")

    # Передаем полный путь к файлу для загрузки
    # os.getcwd() возвращает текущую рабочую директорию, а '\\downloads\\Test.jpg' — это путь к файлу, который вы хотите загрузить
    # os.path.join() лучше использовать для корректной работы с путями, независимо от операционной системы
    upload_button.send_keys(os.path.join(os.getcwd(), 'downloads', 'Test.jpg'))

    # Ожидаем 3 секунды, чтобы убедиться, что загрузка завершилась (можно заменить на более надежный способ ожидания)
    time.sleep(3)
