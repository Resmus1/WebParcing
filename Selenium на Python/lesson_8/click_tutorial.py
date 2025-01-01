#  https://stepik.org/lesson/1140250/step/1?unit=1151923

import time  # Импортируем модуль для работы с паузами (время).
from selenium import webdriver  # Импортируем WebDriver для управления браузером.
from webdriver_manager.chrome import ChromeDriverManager  # Импортируем менеджер драйверов для Chrome.
from selenium.webdriver.chrome.service import Service  # Импортируем сервис для работы с драйвером Chrome.

# Устанавливаем и создаем сервис для ChromeDriver с использованием webdriver_manager.
service = Service(ChromeDriverManager().install())

# Используем контекстный менеджер для запуска и автоматического закрытия браузера.
with webdriver.Chrome(service=service) as browser:
    # Загружаем веб-страницу по указанному URL.
    browser.get('https://testautomationpractice.blogspot.com/')

    # Находим кнопку по XPath и кликаем по ней.
    button = browser.find_element('xpath', "//button[@onclick='toggleButton(this)']")
    button.click()

    # Находим поле ввода для email по XPath.
    email_field = browser.find_element('xpath', "//input[@id='email']")

    # Вводим тестовый email в найденное поле.
    email_field.send_keys('test@email.com')

    # Ждем 2 секунды для того, чтобы убедиться, что данные введены.
    time.sleep(2)

    # Очищаем поле ввода (удаляем введенный email).
    email_field.clear()

    # Ждем 2 секунды, чтобы удостовериться, что поле очищено.
    time.sleep(2)
