#  https://stepik.org/lesson/1164782/step/1?unit=1177125

# Импорт необходимых модулей из библиотеки Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Настройка опций для ChromeDriver
chrome_options = Options()
# Запуск браузера в headless-режиме (без графического интерфейса)
chrome_options.add_argument("--headless=new")
# Установка размеров окна браузера
chrome_options.add_argument("--window-size=1920,1080")

# Создание экземпляра веб-драйвера и автоматическое закрытие браузера после выполнения кода
with webdriver.Chrome() as browser:
    # Установка явного ожидания для браузера (максимум 30 секунд)
    wait = WebDriverWait(browser, 30)
    # Открытие веб-страницы с демонстрацией работы с алертами
    browser.get('https://demoqa.com/alerts')

    # Локатор кнопки, которая вызывает подтверждающее окно (alert)
    BUTTON = ('xpath', "//button[@id='confirmButton']")

    # Ожидание, пока кнопка станет кликабельной, и клик по ней
    wait.until(EC.element_to_be_clickable(BUTTON)).click()

    # Ожидание появления алерта
    alert = wait.until(EC.alert_is_present())

    # Переключение на алерт
    browser.switch_to.alert

    # Вывод текста из алерта в консоль
    print(alert.text)

    # Закрытие алерта нажатием на кнопку "Отмена" (dismiss)
    alert.dismiss()
