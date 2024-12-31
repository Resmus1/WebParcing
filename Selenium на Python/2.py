# https://stepik.org/lesson/1140232/step/1?unit=1151905

from selenium import webdriver  # Импортируем основной модуль для работы с браузером
from webdriver_manager.firefox import \
    GeckoDriverManager  # Импортируем GeckoDriverManager для автоматической загрузки драйвера Firefox
from selenium.webdriver.firefox.service import Service  # Импортируем Service для указания пути к драйверу
from selenium.common.exceptions import \
    WebDriverException  # Импортируем исключение, которое возникает при ошибках с драйверами

try:
    # Пытаемся создать экземпляр браузера Firefox без явного указания драйвера
    # Selenium будет искать драйвер по умолчанию
    driver = webdriver.Firefox()

except WebDriverException:
    # Если возникает ошибка, например, драйвер не найден или не может быть загружен,
    # переходим к следующему шагу, чтобы автоматически установить драйвер
    service = Service(
        GeckoDriverManager().install())  # Устанавливаем нужный драйвер для Firefox с помощью GeckoDriverManager
    driver = webdriver.Firefox(service=service)  # Создаем экземпляр браузера Firefox, используя установленные драйверы

# После того как экземпляр драйвера успешно создан, продолжаем работу с браузером
driver.get('https://www.example.com')  # Открываем сайт по URL
