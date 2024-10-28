# https://stepik.org/lesson/732063/step/3?unit=733596

# Импортируем необходимые модули из библиотеки Selenium
from selenium import webdriver

# Создаем объект настроек для Chrome
options_chrome = webdriver.ChromeOptions()
# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome.add_argument('--headless=new')

# Открываем браузер Chrome с заданными настройками и работаем с ним в блоке 'with'
with webdriver.Chrome(options=options_chrome) as browser:
    # Загружаем веб-страницу по указанному URL
    browser.get('https://parsinger.ru/methods/3/index.html')

    # Получаем все cookies, установленные на текущей странице
    cookies = browser.get_cookies()

    # Инициализируем переменную для хранения суммы значений cookies
    sum_cookies = 0

    # Проходим по каждому cookie (каждый cookie представлен в виде словаря)
    for dict_key in cookies:
        # Проверяем, является ли число, стоящее в конце имени cookie, четным
        # Разделяем имя cookie по символу '_', берем последний элемент и проверяем остаток от деления на 2
        if int(dict_key['name'].rsplit('_', 1)[-1]) % 2 == 0:
            # Если условие выполняется, добавляем значение cookie к сумме
            sum_cookies += int(dict_key['value'])

    # Выводим сумму значений cookies, соответствующих заданному условию
    print(sum_cookies)
