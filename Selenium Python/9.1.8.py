#  https://stepik.org/lesson/897512/step/12?unit=1066949

# Импорт необходимых библиотек для работы с Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Устанавливаем опции для браузера
options = Options()
options.add_argument('--headless=new')  # Опция для запуска браузера в фоновом режиме (без интерфейса)

try:
    # Инициализация веб-драйвера
    with webdriver.Chrome(options=options) as browser:
        # Открываем веб-страницу
        browser.get('https://parsinger.ru/selenium/5.10/8/index.html')

        # Находим все элементы для перемещения с классом 'piece'
        boxes = browser.find_elements(By.CLASS_NAME, 'piece')

        # Находим все элементы, указывающие на целевые позиции с классом 'range'
        places = browser.find_elements(By.CLASS_NAME, 'range')

        # Находим элемент, который содержит итоговое сообщение
        result = browser.find_element(By.ID, 'message')

        # Перебираем элементы 'boxes' по индексу
        for i in range(len(boxes)):
            # Перетаскиваем каждый элемент box вместо, указанное элементом place
            # Извлекаем числовое значение смещения из текста элемента 'range'
            ActionChains(browser).drag_and_drop_by_offset(
                boxes[i],  # Исходный элемент для перемещения
                int(places[i].text[-5:-2]),  # Смещение по X (последние три символа текста указывают смещение)
                0  # Смещение по Y (здесь оно равно 0, так как перемещение только по горизонтали)
            ).release().perform()  # Завершаем действие

        # Выводим текст итогового сообщения
        print(result.text)

# Обрабатываем исключения, чтобы понять причину ошибки, если она возникнет
except Exception as e:
    print(f"Alert: {e}")  # Выводим сообщение об ошибке
