# https://stepik.org/lesson/731861/step/6?unit=733396

# Импортируем необходимые модули из библиотеки Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер Chrome и работаем с ним в блоке 'with'
with webdriver.Chrome() as browser:
    # Загружаем веб-страницу по указанному URL
    browser.get('http://parsinger.ru/selenium/3/3.html')

    # Находим все элементы на странице, которые имеют тег <p>
    all_nums = browser.find_elements(By.TAG_NAME, 'p')

    # Переменная для хранения суммы всех чисел
    num_sum = 0

    # Проходим по каждому найденному элементу
    for num in all_nums:
        # Преобразуем текст элемента в целое число и добавляем его к сумме
        num_sum += int(num.text)

    # Выводим итоговую сумму в консоль
    print(num_sum)
    