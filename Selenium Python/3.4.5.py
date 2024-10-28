# https://stepik.org/lesson/731861/step/8?unit=733396

# Импортируем необходимые модули из библиотеки Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер Chrome и работаем с ним в блоке 'with'
with webdriver.Chrome() as browser:
    # Загружаем веб-страницу по указанному URL
    browser.get('https://parsinger.ru/selenium/4/4.html')

    # Находим все элементы с классом 'check' (чекбоксы) на странице
    check_box = browser.find_elements(By.CLASS_NAME, 'check')

    # Проходим по каждому найденному чекбоксу и кликаем по нему
    for check in check_box:
        check.click()  # Отмечаем чекбокс

    # Находим кнопку с классом 'btn' и кликаем по ней для отправки формы
    browser.find_element(By.CLASS_NAME, 'btn').click()

    # Находим элемент с ID 'result', получаем его текст и выводим в консоль
    print(browser.find_element(By.ID, 'result').text)
