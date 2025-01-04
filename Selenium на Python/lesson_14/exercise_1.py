#  https://stepik.org/lesson/1164785/step/1?unit=1177128

from selenium import webdriver

# Создаём объект ChromeOptions для настройки браузера
chrome_options = webdriver.ChromeOptions()
# Включаем headless режим для запуска браузера без графического интерфейса
chrome_options.add_argument('--headless=new')

# Создаём экземпляр браузера с указанными опциями
with webdriver.Chrome(options=chrome_options) as browser:
    # Открываем указанную страницу
    browser.get('https://the-internet.herokuapp.com/')

    # Создаём cookie с обязательными параметрами: имя и значение
    cookie = {
        'name': 'username',  # Имя cookie
        'value': 'user123'  # Значение cookie
    }

    # Получаем список текущих cookies, установленных для страницы
    cookies = browser.get_cookies()

    # Добавляем созданное cookie в браузер
    browser.add_cookie(cookie)

    # Получаем обновлённый список cookies после добавления нового
    new_cookies = browser.get_cookies()

    # Убеждаемся, что список cookies изменился после добавления нового
    # Если нет, будет выброшено исключение AssertionError с сообщением "Cookies No ADD"
    assert cookies != new_cookies, "Cookies No ADD"

    # Если всё прошло успешно, выводим сообщение
    print('Done')
