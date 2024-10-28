# https://stepik.org/lesson/731861/step/11?unit=733396

# Импортируем необходимые модули из библиотеки Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер Chrome и работаем с ним в блоке 'with'
with webdriver.Chrome() as browser:
    # Загружаем веб-страницу по указанному URL
    browser.get('https://parsinger.ru/selenium/6/6.html')

    # Получаем текст из элемента с ID 'text_box', вычисляем его значение с помощью eval
    ex = eval(browser.find_element(By.ID, 'text_box').text)

    # Находим все элементы с тегом 'option' (элементы выпадающего списка)
    l_num = browser.find_elements(By.TAG_NAME, 'option')

    # Проходим по каждому элементу списка
    for num in l_num:
        # Проверяем, равен ли текст элемента значению ex
        if int(num.text) == ex:
            # Если равен, кликаем по этому элементу
            num.click()
            # Находим кнопку с классом 'btn' и кликаем по ней для отправки формы
            browser.find_element(By.CLASS_NAME, 'btn').click()
            # Получаем текст результата и выводим его в консоль
            print(browser.find_element(By.ID, 'result').text)
            # Выходим из цикла после нахождения и клика по нужному элементу
            break
