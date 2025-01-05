#  https://stepik.org/lesson/1164788/step/1?unit=1177131

from selenium import webdriver
from selenium.webdriver.support.select import Select

# Указываем настройки для запуска браузера в headless-режиме (без графического интерфейса)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless=new")

# Локатор для выбора элемента выпадающего списка
SELECT_LOCATOR = ("xpath", "//select[@id='dropdown']")

# Создаём браузерный драйвер и открываем его в контексте `with`
with webdriver.Chrome(options=chrome_options) as browser:
    try:
        # Переходим на тестовую страницу
        browser.get("https://the-internet.herokuapp.com/dropdown")

        # Находим элемент выпадающего списка и инициализируем объект Select для управления им
        DROPDOWN = Select(browser.find_element(*SELECT_LOCATOR))

        # Получаем все доступные опции из выпадающего списка
        all_options = DROPDOWN.options

        # Тест 1: Выбор опции по видимому тексту (select_by_visible_text)
        for option in all_options:
            if option.is_enabled():  # Проверяем, что опция не отключена
                DROPDOWN.select_by_visible_text(option.text)  # Выбираем опцию по тексту
                print(f"{option.text} Selected")  # Печатаем выбранную опцию
        print("Test text Complete\n")  # Сообщаем о завершении теста

        # Тест 2: Выбор опции по индексу (select_by_index)
        for index, option in enumerate(all_options):  # Используем enumerate для получения индекса
            if option.is_enabled():  # Проверяем, что опция не отключена
                DROPDOWN.select_by_index(index)  # Выбираем опцию по её индексу
                print(f"{option.text} Selected")  # Печатаем выбранную опцию
        print("Test index Complete\n")  # Сообщаем о завершении теста

        # Тест 3: Выбор опции по значению (select_by_value)
        for option in all_options:
            if option.is_enabled():  # Проверяем, что опция не отключена
                DROPDOWN.select_by_value(option.get_attribute('value'))  # Выбираем опцию по значению
                print(f"{option.text} Selected")  # Печатаем выбранную опцию
        print("Test value Complete\n")  # Сообщаем о завершении теста

    except Exception as e:
        # Обрабатываем исключения и выводим сообщение об ошибке
        print(f"ERROR: {e}")
