#  https://stepik.org/lesson/897512/step/10?unit=1066949
#  Усложнил, предположил что там весь список рандомный и нужно перевести цвет для его нахождения

import webcolors  # Импортируем библиотеку для работы с цветами
import random  # Импортируем библиотеку для случайных операций (например, перемешивание)
from selenium import webdriver  # Импортируем WebDriver для управления браузером
from selenium.webdriver.chrome.options import Options  # Импортируем настройки для работы с Chrome
from selenium.webdriver.common.action_chains import ActionChains  # Для выполнения цепочек действий (например, drag and drop)
from selenium.webdriver.common.by import By  # Для поиска элементов на странице

# Создаем объект настроек для браузера
options = Options()
options.add_argument('--headless=new')  # Запуск браузера в фоновом режиме без открытия окна

try:
    # Создаем и запускаем браузер с установленными настройками
    with webdriver.Chrome(options=options) as browser:
        # Открываем целевую страницу
        browser.get('https://parsinger.ru/selenium/5.10/3/index.html')

        # Находим все элементы с классом 'draganddrop' (это элементы, которые нужно перетащить)
        boxes = browser.find_elements(By.CLASS_NAME, 'draganddrop')

        # Находим все элементы с классом 'draganddrop_end' (это контейнеры, куда нужно перетащить элементы)
        frames = browser.find_elements(By.CLASS_NAME, 'draganddrop_end')

        # Находим элемент, который будет содержать результат операции (обычно это сообщение)
        result = browser.find_element(By.ID, 'message')

        # Перемешиваем списки элементов случайным образом
        random.shuffle(boxes)
        random.shuffle(frames)

        # Проходим по всем элементам, которые нужно перетащить
        for box in boxes:
            # Получаем стиль элемента
            style_box = box.get_attribute('style')

            # Проверяем, есть ли в стиле цвета в формате rgb
            if 'rgb' in style_box:
                # Извлекаем строку с значениями RGB
                start = style_box.find('rgb')
                end = style_box.find(')')
                rgb_value = style_box[start + 4: end]

                # Преобразуем строку RGB в кортеж из чисел
                rgb_tuple = tuple(map(int, rgb_value.split(',')))

                # Преобразуем RGB в название цвета
                color_box = webcolors.rgb_to_name(rgb_tuple)
            else:
                # Если цвет не в формате RGB, извлекаем значение цвета как строку
                start = style_box.find(': ') + 2
                end = style_box.find(';')
                color_box = style_box[start:end]

            # Проходим по всем контейнерам, в которые нужно перетащить элементы
            for frame in frames:
                # Получаем стиль каждого контейнера
                style_frame = frame.get_attribute('style')

                # Извлекаем цвет из стиля контейнера
                start = style_frame.find(': ') + 2
                end = style_frame.find(';')
                color_frame = style_frame[start:end]

                # Если цвета совпадают, выполняем перетаскивание
                if color_box == color_frame:
                    # Выполняем действие drag and drop
                    ActionChains(browser).drag_and_drop(box, frame).release().perform()

                    # Удаляем контейнер из списка, так как он уже был использован
                    frames.remove(frame)

        # После выполнения всех действий выводим текст результата на экран
        print(result.text)

# Если возникает ошибка, выводим сообщение об ошибке
except Exception as e:
    print(f"Alert: {e}")
