# Импорт необходимых модулей из библиотеки Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка опций для ChromeDriver
chrome_options = Options()
# Запуск браузера в режиме headless (без графического интерфейса, экономит ресурсы)
chrome_options.add_argument("--headless=new")
# Установка размеров окна браузера
chrome_options.add_argument("--window-size=1920,1080")
# Отключение обнаружения браузера как автоматизированного
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# Установка кастомного User-Agent, чтобы сайт воспринимал браузер как обычный пользователь
chrome_options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)

# Создание экземпляра веб-драйвера с заданными опциями и автоматическое закрытие браузера после выполнения кода
with webdriver.Chrome(options=chrome_options) as browser:
    # Установка явного ожидания для браузера с интервалом опроса 0.5 секунды
    wait = WebDriverWait(browser, 30, 0.5)
    # Открытие веб-страницы, чтобы узнать IP-адрес
    browser.get("https://whatismyipaddress.com/")

    # Ожидание, пока заголовок страницы станет ожидаемым
    wait.until(EC.title_is("What Is My IP Address - See Your Public Address - IPv4 & IPv6"))

    # Сохранение скриншота страницы в файл 'screen.png'
    browser.save_screenshot('screen.png')
