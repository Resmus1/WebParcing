#  https://stepik.org/lesson/1164773/step/1?unit=1177117

from selenium import webdriver  # Импортируем WebDriver для управления браузером.

# Создаем объект настроек для ChromeDriver.
chrome_options = webdriver.ChromeOptions()

# Устанавливаем стратегию загрузки страницы:
# 'eager' — WebDriver продолжает выполнение скрипта, как только основная часть страницы загружена, без ожидания загрузки изображений.
chrome_options.page_load_strategy = 'eager'

# Настройки браузера:
chrome_options.add_argument('--headless=new')  # Запуск в безголовом режиме (без графического интерфейса).
chrome_options.add_argument('--disable-gpu')  # Отключение GPU (полезно для headless режима).
chrome_options.add_argument('--start-maximized')  # Открытие браузера в полноэкранном режиме.
chrome_options.add_argument('--window-size=700,700')  # Установка размера окна браузера (ширина 700px, высота 700px).
chrome_options.add_argument('--incognito')  # Запуск в режиме инкогнито.
chrome_options.add_argument('--ignore-certificate-errors')  # Игнорирование ошибок SSL-сертификатов.
chrome_options.add_argument('--disable-cache')  # Отключение кэширования для получения свежих данных.
chrome_options.add_argument('--user-data-dir=<path>')  # Использование указанного пути для пользовательского профиля.

# Используем контекстный менеджер для автоматического закрытия браузера.
with webdriver.Chrome(options=chrome_options) as browser:
    # Загружаем указанную веб-страницу.
    browser.get('https://github.com/Resmus1/WebParcing')
