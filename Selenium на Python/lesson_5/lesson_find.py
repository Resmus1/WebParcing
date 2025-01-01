#  https://stepik.org/lesson/1140222/step/1?unit=1151895

import time
from selenium import webdriver  # Импортируем веб-драйвер для управления браузером
from selenium.webdriver.support import expected_conditions as EC  # Для работы с условиями ожидания
from selenium.webdriver.support.ui import WebDriverWait  # Для реализации явного ожидания

# Открываем браузер в контексте (автоматически закроется после выполнения кода)
with webdriver.Chrome() as browser:
    # Открываем страницу
    browser.get('https://github.com/Resmus1/WebParcing')

    # Явное ожидание: ждём до 10 секунд с интервалом 0.5 секунды, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 10, 0.5).until(
        EC.element_to_be_clickable(('xpath', '//*[@id=":R55ab:"]'))  # Ищем кнопку по XPath
    )

    # Нажимаем на найденную кнопку
    button.click()

    # Ждём 2 секунды после клика, чтобы увидеть результат
    time.sleep(2)

    # Повторный клик по кнопке
    button.click()

    # Ждём ещё 2 секунды, чтобы завершить выполнение
    time.sleep(2)
