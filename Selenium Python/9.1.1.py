#  https://stepik.org/lesson/897512/step/5?unit=1066949

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

try:
    # Создание экземпляра веб-драйвера с заданными опциями
    with webdriver.Chrome() as browser:
        # Открытие локальной HTML страницы
        browser.get("https://parsinger.ru/selenium/5.10/9/index.html")

        # Поиск элемента (квадрата) на странице
        square = browser.find_element(By.CSS_SELECTOR, "canvas")

        # Создание объекта ActionChains для выполнения действий с элементами
        actions = ActionChains(browser)

        # Передвижение квадрата на указанные координаты
        actions.click_and_hold(square).move_by_offset(100, -100).release().perform()

        # Пауза для визуальной проверки результата
        time.sleep(5)


except Exception as e:
    # Обработка возможных исключений и вывод сообщения об ошибке
    print(f'Alert: {e}')
