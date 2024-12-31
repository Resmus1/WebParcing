#  https://stepik.org/lesson/897512/step/11?unit=1066949

# Импортируем необходимые библиотеки и модули
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Настройки для запуска браузера в режиме без интерфейса (headless)
options = Options()
options.add_argument('--headless=new')  # Запуск Chrome в фоновом режиме (без GUI)

try:
    # Инициализируем драйвер браузера
    with webdriver.Chrome(options=options) as browser:

        # Переходим на нужную веб-страницу
        browser.get('https://parsinger.ru/selenium/5.10/4/index.html')

        # Ищем все элементы, которые представляют мячи (по классу 'ball_color')
        balls = browser.find_elements(By.CLASS_NAME, 'ball_color')

        # Ищем все элементы, которые представляют корзины (по классу 'basket_color')
        boxes = browser.find_elements(By.CLASS_NAME, 'basket_color')

        # Ищем элемент, который отображает результат
        result = browser.find_element(By.CLASS_NAME, 'message')

        # Для каждой корзины (box) получаем её цвет фона
        for box in boxes:
            box_color = box.value_of_css_property('background-color')  # Извлекаем цвет фона корзины

            # Для каждого мяча (ball) сравниваем его цвет с цветом корзины
            for ball in balls:
                ball_color = ball.value_of_css_property('background-color')  # Извлекаем цвет фона мяча

                # Если цвета мяча и корзины совпадают, выполняем перетаскивание мяча в корзину
                if ball_color == box_color:
                    # Действие: нажать на мяч, перетащить в корзину и отпустить
                    ActionChains(browser).drag_and_drop(ball, box).release().perform()

        # После выполнения всех действий выводим результат на экран
        print(result.text)

except Exception as e:
    # В случае ошибки выводим сообщение
    print(f"Alert: {e}")
