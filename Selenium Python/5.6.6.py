# https://stepik.org/lesson/732063/step/7?unit=733596

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
    browser.get('https://parsinger.ru/scroll/4/index.html')

    # Находим все элементы на странице с классом 'btn'
    elements = browser.find_elements(By.CLASS_NAME, 'btn')

    # Инициализируем переменную для хранения суммы результатов
    result_sum = 0

    # Проходим по каждому элементу (кнопке) в списке
    for btn in elements:
        # Прокручиваем страницу так, чтобы текущая кнопка стала видимой
        browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
        # Кликаем по кнопке
        btn.click()
        # Получаем значение элемента с ID 'result' и добавляем его к сумме
        result_sum += int(browser.find_element(By.ID, 'result').text)

    # Выводим итоговую сумму
    print(result_sum)
