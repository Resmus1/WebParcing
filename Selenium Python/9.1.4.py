#  https://parsinger.ru/selenium/5.10/2/index.html

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
        # Переход на указанную веб-страницу
        browser.get('https://parsinger.ru/selenium/5.10/2/index.html')

        # Поиск всех элементов с классом "draganddrop"
        boxes = browser.find_elements(By.CLASS_NAME, 'draganddrop')

        # Поиск элемента, являющегося конечной точкой перетаскивания
        finish = browser.find_element(By.CLASS_NAME, 'draganddrop_end')

        # Поиск элемента, который отображает результат
        result = browser.find_element(By.ID, 'message')

        # Цикл для выполнения действий с каждым элементом из списка "boxs"
        for box in boxes:
            # Перетаскивание элемента на конечную точку
            ActionChains(browser).click_and_hold(box).move_to_element(finish).release().perform()

        # Печать текста результата, если он обновился
        print(result.text)

# Обработка ошибок и вывод сообщения об исключении
except Exception as e:
    print(f'Alert: {e}')
