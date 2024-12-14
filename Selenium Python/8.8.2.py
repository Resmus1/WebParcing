#  https://stepik.org/lesson/732083/step/2?unit=733616

# Импортируем необходимые модули из Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Настройка параметров запуска браузера
options = Options()
# Указываем, что браузер будет работать в режиме "headless" (без графического интерфейса)
options.add_argument('--headless=new')

if __name__ == '__main__':
    try:
        # Создаем экземпляр веб-драйвера Chrome с заданными параметрами
        with webdriver.Chrome(options=options) as browser:
            # Открываем веб-страницу
            browser.get('https://parsinger.ru/expectations/4/index.html')

            # Явное ожидание: ждем, пока кнопка с ID 'btn' станет кликабельной, и кликаем по ней
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'btn'))).click()

            # Явное ожидание: проверяем, содержит ли заголовок страницы заданную подстроку ('JK8HQ')
            # Параметр poll_frequency=0.1 уменьшает интервал между проверками (по умолчанию 0.5 сек)
            contain = WebDriverWait(browser, 30, poll_frequency=0.1).until(EC.title_contains('JK8HQ'))

            # Если заголовок содержит нужную подстроку, выводим его в консоль
            if contain:
                print(browser.title)

    except Exception as e:
        # Обрабатываем возможные исключения и выводим сообщение об ошибке
        print(f"Alert: {e}")

