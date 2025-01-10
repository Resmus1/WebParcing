#  https://stepik.org/lesson/1189859/step/1?unit=1202808

import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from scrolls import Scrolls

# Настройка опций для браузера Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")  # Установка размера окна браузера.

# Локатор для элемента с текстом "Example 2: "
EX_2_LOCATOR = ("xpath", "//h3[text()='Example 2: ']")

# Открытие браузера с использованием контекстного менеджера
with webdriver.Chrome(options=chrome_options) as browser:
    actions = ActionChains(browser)  # Создание объекта ActionChains для сложных действий.
    scrolls = Scrolls(browser, actions)  # Создание объекта Scrolls для управления прокруткой.

    try:
        # Открытие веб-страницы.
        browser.get("https://seiyria.com/bootstrap-slider/")

        # Поиск элемента с текстом "Example 2: ".
        EX_2 = browser.find_element(*EX_2_LOCATOR)

        # Прокрутка страницы до низа.
        scrolls.scroll_to_bottom()
        time.sleep(2)  # Ожидание для визуального эффекта.

        # Прокрутка страницы до верха.
        scrolls.scroll_to_top()
        time.sleep(2)  # Ожидание для визуального эффекта.

        # Прокрутка страницы на 900 пикселей вниз.
        scrolls.scroll_by(0, 900)
        time.sleep(2)  # Ожидание для визуального эффекта.

        # Прокрутка до элемента EX_2.
        scrolls.scroll_to_element(EX_2)
        time.sleep(2)  # Ожидание для визуального эффекта.

    except Exception as e:
        # Обработка ошибок, если что-то пошло не так.
        print(f"ERROR: {e}")
