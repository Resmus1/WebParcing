#  https://stepik.org/lesson/1164785/step/1?unit=1177128

from selenium import webdriver

# Создаём объект ChromeOptions для настройки браузера
chrome_options = webdriver.ChromeOptions()

# Включаем headless режим для запуска браузера без графического интерфейса
chrome_options.add_argument('--headless=new')

# Запускаем браузер с указанными настройками
with webdriver.Chrome(options=chrome_options) as browser:
    # Открываем указанную веб-страницу
    browser.get('https://the-internet.herokuapp.com/')

    # Получаем список текущих cookies, установленных для страницы
    cookies = browser.get_cookies()

    # Удаляем cookie по имени, взятому из списка cookies (третьего элемента)
    # cookies[2]['name'] указывает на имя третьего cookie в списке (индексация с нуля)
    browser.delete_cookie(cookies[2]['name'])

    # Получаем обновлённый список cookies после удаления
    new_cookies = browser.get_cookies()

    # Проверяем, что список cookies изменился после удаления одного из них
    # Если списки совпадают, выбрасывается исключение AssertionError с сообщением "Cookies no change"
    assert cookies != new_cookies, "Cookies no change"

    # Если все проверки прошли успешно, выводим сообщение
    print('Done')
