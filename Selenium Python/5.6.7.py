# https://stepik.org/lesson/732063/step/8?unit=733596

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
    browser.get('https://parsinger.ru/selenium/5.5/3/1.html')

    # Находим все элементы с классом 'parent' на странице
    elements = browser.find_elements(By.CLASS_NAME, 'parent')

    # Инициализируем переменную для хранения суммы результатов
    result_sum = 0

    # Проходим по каждому элементу (блоку) в списке
    for box in elements:
        # Проверяем, выбран ли чекбокс в данном блоке
        if box.find_element(By.CLASS_NAME, 'checkbox').is_selected():
            # Если чекбокс выбран, извлекаем текст из элемента <textarea> и добавляем его к сумме
            result_sum += int(box.find_element(By.TAG_NAME, 'textarea').text)

    # Выводим итоговую сумму
    print(result_sum)

