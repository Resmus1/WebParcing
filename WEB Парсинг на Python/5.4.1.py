# https://stepik.org/lesson/731861/step/4?unit=733396

# Импортируем необходимые модули из библиотеки Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер Chrome и работаем с ним в блоке 'with'
with webdriver.Chrome() as browser:
    # Переходим на указанный URL
    browser.get('https://parsinger.ru/selenium/1/1.html')

    # Находим все элементы с классом 'form' на странице
    input_form = browser.find_elements(By.CLASS_NAME, 'form')

    # Проходим по каждому найденному элементу и вводим текст 'Текст'
    for i in input_form:
        i.send_keys('Текст')

    # Находим кнопку с ID 'btn' и кликаем по ней
    browser.find_element(By.ID, 'btn').click()

    # Находим элемент с ID 'result' и выводим его текстовое содержимое в консоль
    print(browser.find_element(By.ID, 'result').text)
