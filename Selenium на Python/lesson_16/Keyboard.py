#  https://stepik.org/lesson/1164787/step/1?unit=1177130

from selenium import webdriver
from selenium.webdriver import Keys

# Создание экземпляра браузера с опцией запуска в headless-режиме (без графического интерфейса)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless=new")

# Локаторы для поиска элементов на странице
SELECT_LOCATOR = ("id", "react-select-3-input")  # Локатор для обычного select элемента
MULTISELECT_LOCATOR = ("id", "react-select-4-input")  # Локатор для multiselect элемента
VALUE_SELECT_1 = ("xpath", "//div[@class=' css-1uccc91-singleValue']")  # Локатор для выбранного значения в select
MULTISELECT_VALUE_GREEN = ("xpath", "//div[@class='css-12jo7m5']")  # Локатор для выбранного значения в multiselect (зеленый цвет)

# Запуск браузера
with webdriver.Chrome(options=chrome_options) as browser:
    try:
        # Открытие целевой страницы
        browser.get("https://demoqa.com/select-menu")

        # Поиск обычного select элемента (ввод "Ms." и выбор этого значения)
        select = browser.find_element(*SELECT_LOCATOR)
        select.send_keys("Ms.")  # Ввод текста "Ms." в поле select
        select.send_keys(Keys.ENTER)  # Нажатие Enter для выбора элемента

        # Поиск элемента, отображающего выбранное значение в select
        value = browser.find_element(*VALUE_SELECT_1)

        # Проверка, что выбранное значение соответствует ожидаемому
        assert value.text == "Ms.", "Selected no select Ms."  # Если текст не совпадает, выводится сообщение об ошибке
        print('Done, select Ms.')  # Если проверка прошла успешно, выводим сообщение

        # Поиск элемента multiselect (многоразового выбора) и выбор значения "Green"
        multiselect = browser.find_element(*MULTISELECT_LOCATOR)
        multiselect.send_keys("Gre")  # Ввод текста "Gre" в поле multiselect
        multiselect.send_keys(Keys.TAB)  # Нажатие Tab для выбора значения

        # Поиск элемента, отображающего выбранное значение в multiselect
        multiselect_value = browser.find_element(*MULTISELECT_VALUE_GREEN)

        # Проверка, что выбранное значение соответствует ожидаемому
        assert multiselect_value.text == "Green", "MultiSelect no select Green"  # Если текст не совпадает, выводится сообщение об ошибке
        print('Done, select Green')  # Если проверка прошла успешно, выводим сообщение

    except Exception as e:
        # Обработка ошибок, если что-то пошло не так
        print(f"ERROR: {e}")
