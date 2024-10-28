# https://stepik.org/lesson/732063/step/5?unit=733596

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
    browser.get('https://parsinger.ru/methods/5/index.html')

    # Получаем список всех ссылок (URL), найденных на странице, используя тег 'a'
    l_href = [item.get_attribute('href') for item in browser.find_elements(By.TAG_NAME, 'a')]

    # Инициализируем переменные для хранения максимального значения expiry и соответствующего результата
    expiry = 0
    result = 0

    # Проходим по каждой ссылке в списке
    for link in l_href:
        # Переходим на страницу по текущей ссылке
        browser.get(link)
        # Получаем все cookies, установленные на текущей странице
        cookies = browser.get_cookies()
        # Проверяем каждый cookie
        for key in cookies:
            # Сравниваем значение 'expiry' текущего cookie с сохраненным максимальным значением
            if key['expiry'] > expiry:
                # Если 'expiry' больше, обновляем переменную result, взяв текст элемента с ID 'result'
                result = browser.find_element(By.ID, 'result').text
                # Обновляем максимальное значение 'expiry'
                expiry = key['expiry']

    # Выводим результат
    print(result)
