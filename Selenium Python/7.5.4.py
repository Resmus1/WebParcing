#  https://stepik.org/lesson/732079/step/4?unit=733612

from selenium import webdriver
from selenium.webdriver.common.by import By

# Главная точка входа программы
if __name__ == '__main__':
    try:
        with webdriver.Chrome() as browser:
            # Открываем нужную страницу
            browser.get('https://parsinger.ru/window_size/1/')
            size = 555

            # Получение размеров панели и элементов браузера
            width = browser.get_window_size()['width']
            height = browser.get_window_size()['height']
            work_width = browser.execute_script("return window.innerWidth;") + 2
            work_height = browser.execute_script("return window.innerHeight;") + 2
            diff_width = width - work_width
            diff_height = height - work_height

            # Задаем точные размеры рабочей области
            browser.set_window_size(size + diff_width, size + diff_height)

            # Находим результат
            result = browser.find_element(By.ID, 'result').text
            if result:
                print(result)

    # Обрабатываем любые ошибки, которые могут возникнуть в процессе выполнения программы
    except Exception as e:
        # Выводим сообщение об ошибке в терминал
        print(f"Ошибка: {e}")
