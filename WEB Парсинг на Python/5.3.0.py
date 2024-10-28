# Добавление расширения в браузер Chrome.

import time
import os
from selenium import webdriver

# Получаем абсолютный путь к файлу расширения
extension_path = os.path.join(os.path.dirname(__file__), 'Extensions', 'Mouse Coordinates', '0.2_0.crx')

# Создаем объект ChromeOptions
options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension(extension_path)

# Открываем браузер с использованием настроек
with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)
    time.sleep(50)
