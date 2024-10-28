# https://stepik.org/lesson/732063/step/1?unit=733596

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
    browser.get('https://parsinger.ru/methods/1/index.html')

    # Получаем текст из элемента с ID 'result'
    code = browser.find_element(By.ID, 'result').text

    # Пока текст равен 'refresh page', продолжаем обновлять страницу
    while code == 'refresh page':
        # Обновляем страницу
        browser.refresh()
        # Снова получаем текст из элемента с ID 'result' после обновления страницы
        code = browser.find_element(By.ID, 'result').text

        # Если текст больше не равен 'refresh page', выводим его
        if code != 'refresh page':
            print(code)
