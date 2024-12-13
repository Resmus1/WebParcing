#  https://stepik.org/lesson/732083/step/1?unit=733616

# Импортируем необходимые модули из Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Создаем объект для настроек браузера Chrome
options = Options()
# Добавляем аргумент для запуска браузера в безголовом режиме (headless)
options.add_argument('--headless=new')

if __name__ == '__main__':
    try:
        # Инициализируем веб-драйвер Chrome
        browser = webdriver.Chrome()
        # Открываем указанную веб-страницу
        browser.get('https://parsinger.ru/expectations/3/index.html')

        # Ожидаем, пока кнопка с ID 'btn' станет кликабельной (максимум 10 секунд) и кликаем по ней
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'btn'))).click()

        # Ожидаем изменения заголовка страницы на '345FDG3245SFD' (максимум 30 секунд)
        WebDriverWait(browser, 30).until(EC.title_is('345FDG3245SFD'))

        # Извлекаем текст элемента с ID 'result' и выводим его в консоль
        print(browser.find_element(By.ID, 'result').text)
    except Exception as e:
        # Обрабатываем любые исключения и выводим их в консоль для отладки
        print(f"Alert: {e}")
