#  https://stepik.org/lesson/1140231/step/1?unit=1151904

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import \
    WebDriverException  # Импортируем исключение для обработки ошибок при создании драйвера

try:
    # Пытаемся создать экземпляр браузера Chrome без указания драйвера
    # Selenium будет искать подходящий драйвер автоматически
    driver = webdriver.Chrome()

except WebDriverException:
    # Если возникла ошибка (например, драйвер не найден), переходим к следующему шагу
    # Здесь мы используем WebDriver Manager, чтобы автоматически скачать и установить нужный драйвер
    service = Service(ChromeDriverManager().install())  # Устанавливаем драйвер с помощью webdriver-manager
    driver = webdriver.Chrome(service=service)  # Создаем экземпляр браузера, используя установленный драйвер

# Теперь, когда драйвер успешно создан, можем продолжить взаимодействие с браузером
driver.get('https://www.example.com')  # Открываем нужный сайт
