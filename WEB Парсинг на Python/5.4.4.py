# https://stepik.org/lesson/731861/step/7?unit=733396

# Импортируем необходимые модули из библиотеки Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер Chrome и работаем с ним в блоке 'with'
with webdriver.Chrome() as browser:
    # Загружаем веб-страницу по указанному URL
    browser.get('http://parsinger.ru/selenium/3/3.html')

    # Находим все элементы с классом 'text' на странице и сохраняем их в список
    divs = browser.find_elements(By.CLASS_NAME, 'text')

    # Переменная для хранения суммы чисел из <p> тегов
    p_sum = 0

    # Проходим по каждому найденному элементу div
    for div in divs:
        # Находим второй <p> элемент внутри текущего div и добавляем его текст (число) к сумме
        p_sum += int(div.find_element(By.XPATH, './p[2]').text)

    # Выводим итоговую сумму в консоль
    print(p_sum)
