#  https://stepik.org/lesson/732083/step/6?unit=733616

# Импортируем необходимые библиотеки для работы с Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Создаем объект для конфигурации опций браузера
options = Options()
# Устанавливаем опцию запуска браузера в фоновом режиме (без графического интерфейса)
options.add_argument('--headless=new')

# Основной блок, который будет выполняться
if __name__ == '__main__':
    try:
        # Создаем объект браузера с заданными опциями
        with webdriver.Chrome(options=options) as browser:
            # Переходим на указанный веб-сайт
            browser.get('https://parsinger.ru/selenium/5.9/4/index.html')

            # Закрываем всплывающее окно с классом 'close'
            browser.find_element(By.CLASS_NAME, 'close').click()

            # Ожидаем, пока элемент с классом 'close' исчезнет (всплывающее окно закроется)
            WebDriverWait(browser, 30).until(EC.invisibility_of_element((By.CLASS_NAME, 'close')))

            # Находим и кликаем на кнопку на странице
            browser.find_element(By.TAG_NAME, 'button').click()

            # Получаем и выводим текст сообщения из элемента с ID 'message'
            print(browser.find_element(By.ID, 'message').text)

    except Exception as e:
        # Если возникла ошибка, выводим сообщение об исключении
        print(f"Alert: {e}")

