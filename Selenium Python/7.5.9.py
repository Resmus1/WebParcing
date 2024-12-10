#  https://stepik.org/lesson/732079/step/9?unit=733612

# Импортируем необходимые модули из Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException

# Настраиваем опции для Chrome, чтобы запускать браузер в headless-режиме
options = Options()
options.add_argument('--headless==new')  # '--headless==new' указывает на использование нового режима headless

if __name__ == '__main__':  # Проверяем, что код выполняется как основной модуль
    codes = []  # Список для хранения кодов, которые будем получать из iframe

    try:
        # Запускаем браузер с заданными опциями
        browser = webdriver.Chrome(options=options)

        # Открываем указанную веб-страницу
        browser.get('https://parsinger.ru/selenium/5.8/5/index.html')

        # Находим поле ввода и кнопку для отправки данных
        input_field = browser.find_element(By.ID, 'guessInput')
        enter_button = browser.find_element(By.ID, 'checkBtn')

        # Находим все iframe на странице
        iframes = browser.find_elements(By.TAG_NAME, 'iframe')

        # Цикл по всем iframe
        for iframe in iframes:
            # Переключаемся на текущий iframe
            browser.switch_to.frame(iframe)

            # Нажимаем кнопку внутри iframe, чтобы получить код
            browser.find_element(By.TAG_NAME, 'button').click()

            # Извлекаем текст кода и добавляем его в список
            codes.append(browser.find_element(By.ID, 'numberDisplay').text)

            # Возвращаемся в основной контент страницы
            browser.switch_to.default_content()

        # Переходим к проверке каждого кода из списка
        for code in codes:

            # Ввод кода в поле
            input_field.clear()
            input_field.send_keys(code)

            # Нажимаем кнопку для отправки введенного кода
            enter_button.click()

            try:
                # Пытаемся переключиться на alert, чтобы прочитать его текст
                alert = Alert(browser)
                print(alert.text)  # Выводим текст alert в консоль
            except NoAlertPresentException:
                # Если alert не найден, продолжаем выполнение без остановки
                continue

    except Exception as e:
        # Обрабатываем любые исключения и выводим их в консоль
        print(f"Alert: {e}")
