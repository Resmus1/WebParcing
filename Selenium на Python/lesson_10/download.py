#  https://stepik.org/lesson/1164775/step/1?unit=1177119

import os  # Импортируем модуль для работы с файловой системой
import time  # Импортируем модуль для работы с задержками

from selenium import webdriver  # Импортируем библиотеку Selenium для автоматизации браузера

# Настройка параметров для браузера Chrome
chrom_option = webdriver.ChromeOptions()
chrom_option.page_load_strategy = 'eager'  # Устанавливаем стратегию загрузки страницы: "eager" (ждем, пока основное содержимое загрузится)
chrom_option.add_argument('--headless=new')  # Запускаем браузер в headless-режиме (без графического интерфейса)

# Настраиваем параметры для загрузки файлов
prefs = {
    "download.default_directory": f"{os.path.join(os.getcwd(), 'downloads')}",  # Указываем путь к папке загрузки
}
chrom_option.add_experimental_option('prefs', prefs)  # Передаем настройки загрузки в браузер

# Запуск браузера с указанными настройками
with webdriver.Chrome(options=chrom_option) as browser:
    browser.get('https://the-internet.herokuapp.com/download')  # Открываем веб-страницу с тестовыми файлами для загрузки

    # Ищем все элементы <a> (ссылки) на странице и выбираем 5-ю по индексу (нумерация с 0)
    file = browser.find_elements('xpath', '//a')[4]
    file.click()  # Кликаем по найденной ссылке для начала загрузки файла

    time.sleep(3)  # Даем браузеру время на загрузку файла (нужно заменить на более точный метод ожидания)
