#  https://stepik.org/lesson/1140249/step/1?unit=1151922

from selenium import webdriver  # Импортируем WebDriver для управления браузером.
from selenium.webdriver.chrome.options import Options  # Импортируем класс для настройки браузера.

# Создаем объект настроек для ChromeDriver.
options = Options()
# Добавляем аргумент '--headless=new', чтобы запустить браузер в безголовом режиме (без отображения графического интерфейса).
options.add_argument('--headless=new')

# Используем контекстный менеджер, чтобы автоматически закрыть браузер после выполнения кода.
with webdriver.Chrome(options=options) as browser:
    # Загружаем веб-страницу по указанному URL.
    browser.get('https://hyperskill.org/courses')

    # Находим второй элемент с тегом <a> и классом 'nav-link' с помощью XPath.
    block = browser.find_element('xpath', "(//a[@class='nav-link'])[2]")

    # Находим элемент <span> с текстом строго равным 'JetBrains Academy' с помощью XPath.
    text = browser.find_element('xpath', "//span[text()='JetBrains Academy']")

    # Находим элемент <div>, который содержит класс 'items-center' и текст ' Provided by ' с помощью XPath.
    provided = browser.find_element('xpath', "//div[contains(@class, 'items-center') and text()=' Provided by ']")

    # Печатаем найденные элементы в консоль. Каждый элемент выводится с новой строки.
    print(block, text, provided, sep='\n')
