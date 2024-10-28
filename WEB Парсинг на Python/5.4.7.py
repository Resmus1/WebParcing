# https://stepik.org/lesson/731861/step/10?unit=733396

# Импортируем необходимые модули из библиотеки Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер Chrome и работаем с ним в блоке 'with'
with webdriver.Chrome() as browser:
    # Загружаем веб-страницу по указанному URL
    browser.get('https://parsinger.ru/selenium/7/7.html')

    # Находим все элементы с тегом 'option' на странице (это элементы списка)
    l_num = browser.find_elements(By.TAG_NAME, 'option')

    # Инициализируем переменную для хранения суммы чисел
    sum_num = 0

    # Проходим по каждому элементу списка
    for num in l_num:
        # Преобразуем текст элемента в целое число и добавляем его к сумме
        sum_num += int(num.text)

    # Находим поле ввода по ID 'input_result' и вводим в него сумму
    browser.find_element(By.ID, 'input_result').send_keys(str(sum_num))

    # Находим кнопку с классом 'btn' и кликаем по ней для отправки формы
    browser.find_element(By.CLASS_NAME, 'btn').click()

    # Находим элемент с ID 'result', получаем его текст и выводим в консоль
    print(browser.find_element(By.ID, 'result').text)
