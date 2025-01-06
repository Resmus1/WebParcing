#  https://stepik.org/lesson/1164791/step/1?unit=1177134

from selenium import webdriver

# Настройка опций для браузера Chrome
chrome_options = webdriver.ChromeOptions()
# Запуск браузера в headless-режиме (без графического интерфейса)
chrome_options.add_argument("--headless=new")
# Установка размера окна браузера
chrome_options.add_argument("--window-size=1920,1080")
# Отключаем обнаружение автоматического управления WebDriver
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# Устанавливаем пользовательский User-Agent для эмуляции обычного пользователя
chrome_options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)

# XPath для поиска элемента
ELEMENT = ("xpath", "//div")

# Список URL-адресов для посещения
urls = ['https://hyperskill.org/login', 'https://funpay.com/', 'https://aur.archlinux.org/']
# Список для хранения заголовков страниц
titles = []

# Запуск браузера с указанными опциями
with webdriver.Chrome(options=chrome_options) as browser:
    try:
        # Проходим по списку URL и открываем каждую страницу
        for i, url in enumerate(urls):
            # Открытие страницы
            browser.get(url)
            # Добавляем заголовок страницы в список titles
            titles.append(browser.title)
            # Открытие новой вкладки для следующей страницы
            browser.switch_to.new_window("tab")

        # Закрытие последней вкладки (это не всегда будет актуально, т.к. она не всегда является активной)
        browser.close()
        # Печать заголовков всех открытых страниц
        print(*titles, sep="\n")

        # Получаем список всех открытых вкладок
        handles = browser.window_handles
        for i in range(len(handles)):
            # Переключаемся на вкладку
            browser.switch_to.window(handles[i])
            # Получаем текущий URL вкладки
            url = browser.current_url
            # Находим все элементы на странице, соответствующие XPath
            all_elements = browser.find_elements(*ELEMENT)
            for element in all_elements:
                try:
                    # Пытаемся кликнуть на первый найденный элемент
                    element.click()
                    # Если клик выполнен успешно, выводим сообщение
                    print(f"In tab {url} Click Done")
                    # Прерываем цикл после первого успешного клика
                    break
                except Exception as a:
                    # Обработка ошибок клика (например, если элемент не кликабелен)
                    print(f"ERROR {a}")

    except Exception as e:
        # Обработка ошибок на уровне основной логики (например, если не удалось открыть страницу)
        print(f"ERROR: {e}")
