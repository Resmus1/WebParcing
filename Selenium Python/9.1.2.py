#  https://stepik.org/lesson/897512/step/6?unit=1066949

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Настройка опций для браузера Chrome
options = Options()
options.add_argument('--headless=new')  # Запуск браузера в безголовом режиме (без интерфейса)

try:
    # Создание экземпляра веб-драйвера с заданными опциями
    with webdriver.Chrome(options=options) as browser:
        # Переход на указанную веб-страницу
        browser.get('https://parsinger.ru/draganddrop/1/index.html')

        # Поиск элементов на странице
        square = browser.find_element(By.ID, 'draggable')  # Элемент, который нужно перетащить
        place = browser.find_element(By.ID, 'field2')  # Место, куда нужно перетащить элемент
        result = browser.find_element(By.ID, 'result')  # Элемент для отображения результата

        # Выполнение действия "перетащить и отпустить"
        ActionChains(browser).click_and_hold(square).move_to_element(place).release().perform()

        # Вывод текста из элемента результата
        print(result.text)

except Exception as e:
    # Обработка возможных исключений и вывод сообщения об ошибке
    print(f'Alert: {e}')
