#  # Импортируем модуль webdriver из библиотеки Selenium

# Импортируем необходимые модули из библиотеки Selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Открываем браузер Chrome в контексте менеджера (он автоматически закроется после выхода из блока with)
with webdriver.Chrome() as browser:
    # Переходим на страницу с динамическими элементами
    browser.get('https://the-internet.herokuapp.com/dynamic_controls')

    # Создаем объект WebDriverWait для задания ожиданий (максимум 30 секунд, проверка каждые 0.5 секунды)
    wait = WebDriverWait(browser, 30, 0.5)

    # Локатор кнопки "Enable" (XPath выражение для поиска элемента)
    ENABLE_BUTTON = ('xpath', "//button[text()='Enable']")
    # Локатор текстового поля (XPath выражение для поиска элемента)
    TEXT_FIELD = ('xpath', "//input[@type='text']")

    # Ждем, пока кнопка "Enable" станет кликабельной, и кликаем по ней
    wait.until(EC.element_to_be_clickable(ENABLE_BUTTON)).click()

    # Ждем, пока текстовое поле станет доступным для ввода, и вводим текст "Hello"
    wait.until(EC.element_to_be_clickable(TEXT_FIELD)).send_keys('Hello')

    # Убеждаемся, что в текстовом поле появился текст "Hello"
    wait.until(EC.text_to_be_present_in_element_value(TEXT_FIELD, 'Hello'))

    # Печатаем сообщение в консоль после успешного выполнения всех действий
    print('Done')
