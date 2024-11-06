# https://stepik.org/lesson/732069/step/5?unit=733602

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

# Используем контекстный менеджер для открытия браузера
with webdriver.Chrome() as browser:
    # Переходим на целевую страницу
    browser.get('https://parsinger.ru/selenium/5.7/1/index.html')
    # Находим все кнопки на странице по тегу <button>
    uran = browser.find_elements(By.TAG_NAME, 'button')

    for u in uran:
        # Прокручиваем страницу до кнопки, чтобы она стала видимой
        browser.execute_script("return arguments[0].scrollIntoView(true);", u)
        # Кликаем по кнопке
        u.click()

    # Получаем текст последнего всплывающего окна alert
    alert_text = Alert(browser).text
    print(alert_text) # Выводим текст alert на экран


