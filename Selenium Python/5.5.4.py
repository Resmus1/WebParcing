# https://stepik.org/lesson/732063/step/4?unit=733596

# Импортируем необходимые модули из библиотеки Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем объект настроек для Chrome
options_chrome = webdriver.ChromeOptions()
# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome.add_argument('--headless=new')

# Открываем браузер Chrome с заданными настройками и работаем с ним в блоке 'with'
with webdriver.Chrome(options=options_chrome) as browser:
    # Загружаем веб-страницу по указанному URL
    browser.get('https://parsinger.ru/selenium/5.5/2/1.html')

    # Находим все элементы, у которых атрибут data-enabled равен "true"
    fields = browser.find_elements(By.XPATH, '//*[@data-enabled="true"]')

    # Проходим по каждому найденному элементу
    for fil in fields:
        # Очищаем содержимое текстового поля
        fil.clear()

    # Находим кнопку с ID 'checkButton' и кликаем по ней
    browser.find_element(By.ID, 'checkButton').click()

    # Переключаемся на появившееся модальное окно (alert) и выводим его текст
    print(browser.switch_to.alert.text)
