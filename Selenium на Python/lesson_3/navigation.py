#  https://stepik.org/lesson/1140224/step/1?unit=1151897

import time  # Импортируем модуль для работы со временем

from selenium import webdriver  # Импортируем webdriver для работы с браузером

try:
    # Открываем браузер Chrome
    with webdriver.Chrome() as browser:
        # Переходим на сайт Google
        browser.get('https://www.google.com/')

        # Переходим на предыдущую страницу (в данном случае это будет пустая история)
        browser.back()
        time.sleep(3)  # Ожидаем 3 секунды, чтобы увидеть изменения

        # Переходим на следующую страницу (возвращаемся на Google)
        browser.forward()
        time.sleep(3)  # Ожидаем 3 секунды

        # Обновляем текущую страницу
        browser.refresh()
        time.sleep(3)  # Ожидаем 3 секунды после обновления страницы
except Exception as e:
    # В случае ошибки выводим сообщение об ошибке
    print(e)
