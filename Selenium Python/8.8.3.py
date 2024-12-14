#  https://stepik.org/lesson/732083/step/3?unit=733616

# Импортируем необходимые модули из Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Настройка параметров для браузера
options = Options()
# Режим headless ("безголовый") позволяет запускать браузер без графического интерфейса
options.add_argument('--headless=new')

if __name__ == '__main__':
    try:
        # Создаем экземпляр веб-драйвера Chrome с заданными параметрами
        with webdriver.Chrome(options=options) as browser:
            # Открываем заданный URL
            browser.get('https://parsinger.ru/expectations/6/index.html')

            # Явное ожидание: ждем, пока кнопка с ID 'btn' станет кликабельной, затем кликаем по ней
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'btn'))).click()

            # Явное ожидание: ждем, пока элемент с классом 'BMH21YY' появится в DOM,
            # и получаем текст из этого элемента
            key = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'BMH21YY'))).text

            # Если текст успешно получен, выводим его в консоль
            if key:
                print(key)

    except Exception as e:
        # Обрабатываем возможные ошибки и выводим сообщение об исключении
        print(f"Alert: {e}")
