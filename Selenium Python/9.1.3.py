#  https://stepik.org/lesson/897512/step/7?unit=1066949

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Настройка опций для браузера Chrome
options = Options()
options.add_argument('--headless=new')  # Запуск браузера в безголовом режиме (без интерфейса)

try:
    # Открываем браузер с заданными опциями
    with webdriver.Chrome(options=options) as browser:
        # Переход на указанную веб-страницу
        browser.get('https://parsinger.ru/draganddrop/3/index.html')

        # Поиск элемента, который нужно перетаскивать
        square = browser.find_element(By.ID, 'block1')

        # Поиск всех целевых точек для перетаскивания
        points = browser.find_elements(By.CSS_SELECTOR, '.controlPoint')

        # Поиск элемента, отображающего результат
        result = browser.find_element(By.ID, 'message')

        # Создание цепочки действий для выполнения drag-and-drop
        action = ActionChains(browser)
        action.click_and_hold(square).perform()  # Захватываем элемент для перетаскивания

        # Перемещение элемента к каждой точке из списка
        for point in points:
            action.move_to_element(point).perform()  # Перетаскивание элемента к точке

        # Завершаем перетаскивание, зафиксировав позицию
        action.move_by_offset(0, 0).perform()  # Движение без смещения (завершение действия)

        # Печать текста результата
        print(result.text)

except Exception as e:
    # Обработка исключений и вывод сообщения об ошибке
    print(f'Alert: {e}')
