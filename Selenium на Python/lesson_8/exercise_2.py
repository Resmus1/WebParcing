#  https://stepik.org/lesson/1140255/step/1?unit=1151928

from selenium import webdriver  # Импортируем WebDriver для управления браузером.
from selenium.webdriver.chrome.options import Options  # Импортируем класс для настройки браузера.

# Создаем объект настроек для ChromeDriver.
options = Options()
# Добавляем аргумент '--headless=new', чтобы запустить браузер в безголовом режиме (без графического интерфейса).
options.add_argument('--headless=new')

# Используем контекстный менеджер для автоматического закрытия браузера по завершению работы.
with webdriver.Chrome(options=options) as browser:
    # Загружаем веб-страницу с кодами статусов.
    browser.get('https://the-internet.herokuapp.com/status_codes')

    # Находим все элементы <a> внутри списка <li>, которые ссылаются на страницы с кодами статусов.
    codes = browser.find_elements('xpath', '//li/a')

    # Для каждого найденного элемента (ссылки на код статуса):
    for code in codes:
        # Кликаем на ссылку, чтобы перейти на страницу с соответствующим кодом статуса.
        code.click()

        # Выводим текущий URL страницы, чтобы убедиться, что мы перешли на нужную страницу.
        print(browser.current_url)

        # Возвращаемся назад на предыдущую страницу (список кодов статусов).
        browser.back()
