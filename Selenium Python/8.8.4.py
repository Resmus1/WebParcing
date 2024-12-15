#  https://stepik.org/lesson/732083/step/4?unit=733616

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Настраиваем опции для веб-драйвера
options = Options()
options.add_argument('--headless=new')  # Запуск браузера в безголовом режиме (без графического интерфейса)

if __name__ == '__main__':  # Проверяем, что скрипт запущен напрямую, а не импортирован как модуль
    try:
        # Создаем веб-драйвер с указанными настройками, используя контекстный менеджер "with"
        with webdriver.Chrome(options=options) as browser:
            # Открываем целевую веб-страницу
            browser.get('https://parsinger.ru/selenium/5.9/2/index.html')

            # Ожидаем появления элемента с ID "qQm9y1rk" и кликаем на него
            WebDriverWait(browser, 120, poll_frequency=0.1).until(
                EC.presence_of_element_located((By.ID, 'qQm9y1rk'))
            ).click()

            # Переключаемся на всплывающее окно (alert) и выводим его текст
            print(browser.switch_to.alert.text)

    except Exception as e:  # Обрабатываем исключения
        # Выводим информацию о возникшей ошибке
        print(f"Alert: {e}")
