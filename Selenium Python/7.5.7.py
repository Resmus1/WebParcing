#  https://stepik.org/lesson/732079/step/7?unit=733612

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Создаём объект опций для Chrome
options = Options()
# Указываем аргумент для работы браузера в фоновом режиме (без графического интерфейса)
options.add_argument('--headless==new')

# Основной блок программы
if __name__ == '__main__':
    try:
        # Инициализируем браузер с заданными опциями
        browser = webdriver.Chrome(options=options)
        # Открываем страницу по указанному URL
        browser.get('https://parsinger.ru/blank/3/index.html')
        # Переменная для суммирования чисел из заголовков
        code = 0

        # Ищем все кнопки на странице по классу "buttons"
        buttons = browser.find_elements(By.CLASS_NAME, 'buttons')
        # Кликаем по каждой кнопке на странице (открываем новые вкладки)
        [button.click() for button in buttons]

        # Перебираем все открытые вкладки
        for x in range(len(browser.window_handles)):
            # Переключаемся на текущую вкладку
            browser.switch_to.window(browser.window_handles[x])
            # Выполняем JavaScript для получения заголовка текущей вкладки
            num_title = browser.execute_script("return document.title;")
            # Проверяем, является ли заголовок числом
            if num_title.isdigit():
                # Если заголовок — число, добавляем его к общей сумме
                code += int(num_title)

        # Выводим сумму всех чисел из заголовков
        print(code)

    except Exception as e:
        # Обрабатываем исключения и выводим сообщение об ошибке
        print(f"Alert: {e}")
