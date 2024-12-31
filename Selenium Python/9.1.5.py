#  https://stepik.org/lesson/897512/step/9?unit=1066949

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Настройка опций для браузера Chrome
options = Options()
options.add_argument('--headless=new')  # Запуск браузера в безголовом режиме (без графического интерфейса)

try:
    # Создание экземпляра браузера Chrome
    with webdriver.Chrome(options=options) as browser:
        # Открытие веб-страницы
        browser.get('https://parsinger.ru/draganddrop/2/index.html')

        # Поиск элемента, который нужно перетаскивать
        square = browser.find_element(By.ID, 'draggable')

        # Поиск всех элементов с классом "box" (цели для перетаскивания)
        boxes = browser.find_elements(By.CLASS_NAME, 'box')

        # Поиск элемента, который отображает сообщение о результате
        result = browser.find_element(By.ID, 'message')

        # Перетаскивание элемента "square" в каждый из боксов "boxes"
        for box in boxes:
            # Используем метод drag_and_drop для перетаскивания
            ActionChains(browser).drag_and_drop(square, box).release().perform()

        # Печать текста из элемента с результатом
        print(result.text)

# Обработка исключений
except Exception as e:
    print(f"Alert: {e}")  # Вывод сообщения об ошибке
