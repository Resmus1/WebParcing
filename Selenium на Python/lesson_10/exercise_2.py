#  https://stepik.org/lesson/1164777/step/1?unit=1177120

import os  # Импортируем модуль для работы с файловой системой
import time  # Импортируем модуль для работы с задержками

from selenium import webdriver  # Импортируем библиотеку Selenium для автоматизации браузера

# Создаем объект настроек для браузера Chrome
chrome_options = webdriver.ChromeOptions()

# Запускаем браузер в headless-режиме (без графического интерфейса), это полезно для автоматизации на сервере или в фоновом режиме
chrome_options.add_argument('--headless=new')

# Настроим путь для загрузки файлов
# Здесь мы указываем папку 'downloads' в текущей рабочей директории с помощью os.getcwd()
preference = {
    "download.default_directory": f"{os.getcwd()}\\downloads",  # Указываем абсолютный путь к папке для загрузки
}

# Передаем настройки для загрузки файлов в Chrome
chrome_options.add_experimental_option('prefs', preference)

# Запускаем браузер с указанными настройками
with webdriver.Chrome(options=chrome_options) as browser:
    # Открываем страницу, с которой будем загружать файлы
    browser.get('https://the-internet.herokuapp.com/download')

    # Находим все ссылки на странице, используя XPath, и выбираем 13-ю ссылку (нумерация начинается с 0)
    file = browser.find_elements('xpath', '//a')[12]

    # Кликаем по ссылке для начала скачивания файла
    file.click()

    # Даем время для завершения загрузки файла (желательно заменить на более точный способ ожидания)
    time.sleep(3)
