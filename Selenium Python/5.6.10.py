# https://stepik.org/lesson/732063/step/11?unit=733596

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

    # Получаем все куки, установленные для текущего домена
    cookies = browser.get_cookies()

    # Инициализируем переменную для хранения суммы значений куки
    sum_cookie = 0

    # Проходим по всем кукам
    for cookie in cookies:
        # Преобразуем значение куки в целое число и добавляем к общей сумме
        sum_cookie += int(cookie['value'])

    # Выводим общую сумму значений всех куки
    print(sum_cookie)
