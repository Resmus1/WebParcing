# https://stepik.org/lesson/731861/step/5?unit=733396

# Импортируем необходимые модули из библиотеки Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер Chrome и работаем с ним в блоке 'with'
with webdriver.Chrome() as browser:
    # Загружаем веб-страницу по указанному URL
    browser.get('http://parsinger.ru/selenium/2/2.html')

    # Находим ссылку по частичному совпадению текста '16243162441624' и кликаем по ней
    browser.find_element(By.PARTIAL_LINK_TEXT, '16243162441624').click()

    # Находим элемент с ID 'result', получаем его текст и выводим в консоль
    print(browser.find_element(By.ID, 'result').text)
