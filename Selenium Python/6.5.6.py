# https://stepik.org/lesson/732069/step/6?unit=733602

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

# Настройки для браузера Chrome
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless=new')  # Запускаем браузер в фоновом режиме (без GUI)

# Используем контекстный менеджер для открытия браузера
with webdriver.Chrome(options=options_chrome) as browser:
    # Переходим на целевую страницу
    browser.get('https://parsinger.ru/selenium/5.7/5/index.html')

    # Находим все кнопки на странице по тегу <button>
    buttons = browser.find_elements(By.TAG_NAME, 'button')

    # Проходим по каждой кнопке
    for button in buttons:
        # Создаем объект ActionChains для выполнения действий с элементом
        action = ActionChains(browser)

        # Нажимаем и удерживаем кнопку, затем паузим на время, равное тексту на кнопке
        # 'button.text' это строка, которая представляет время задержки в секундах
        action.click_and_hold(button).pause(float(button.text)).release(button).perform()

    # Получаем текст последнего всплывающего окна alert
    alert_text = Alert(browser).text  # Считываем текст сообщения из alert
    print(alert_text)  # Выводим текст alert на экран
