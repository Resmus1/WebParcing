# https://stepik.org/lesson/732069/step/7?unit=733602

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

# Запускаем браузер с помощью WebDriver
with webdriver.Chrome() as browser:
    # Переходим на указанную страницу
    browser.get('https://parsinger.ru/selenium/5.7/4/index.html')

    # Находим контейнер, в котором происходит прокрутка
    main_container = browser.find_element(By.ID, 'main_container')

    # Получаем начальную высоту прокручиваемого контейнера
    last_height = browser.execute_script("return arguments[0].scrollHeight", main_container)

    while True:
        # Прокручиваем элемент до конца, устанавливая scrollTop в значение scrollHeight
        browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", main_container)

        # Ждем немного времени, чтобы дать браузеру время на подгрузку контента
        time.sleep(1)  # Увеличьте время ожидания, если контент подгружается медленно

        # Получаем новую высоту прокручиваемого контейнера
        new_height = browser.execute_script("return arguments[0].scrollHeight", main_container)

        # Если высота не изменилась, значит, больше нет новых элементов, которые подгружаются
        if new_height == last_height:
            print("Достигнут конец прокрутки.")

            # Находим все чекбоксы в контейнере
            checkboxes = main_container.find_elements(By.CSS_SELECTOR, "div.child_container input[type='checkbox']")

            # Кликаем по всем чекбоксам, чьи значения четные
            for box in checkboxes:
                if int(box.get_attribute('value')) % 2 == 0:
                    box.click()

            # Находим кнопку для подтверждения действия (например, кнопка "alert")
            main_container.find_element(By.CLASS_NAME, 'alert_button').click()

            # Переходим к всплывающему окну с алертом и получаем текст из этого окна
            alert_text = Alert(browser).text
            print(alert_text)  # Выводим текст алерта

            # Завершаем выполнение цикла
            break

        # Обновляем переменную last_height для следующей итерации
        last_height = new_height
