#  https://stepik.org/lesson/732079/step/5?unit=733612

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

options = Options()
options.add_argument('--headless==new')


def restart_browser():
    """Перезапускает браузер с теми же настройками"""
    print("Перезапуск браузера...")
    browser.quit()
    time.sleep(1)
    return webdriver.Chrome(options=options)


if __name__ == '__main__':
    try:
        browser = webdriver.Chrome(options=options)
        browser.get('https://parsinger.ru/window_size/2/index.html')

        # Рассчитываем поправку на интерфейс
        width = browser.get_window_size()['width']
        height = browser.get_window_size()['height']
        work_width = browser.execute_script("return window.innerWidth") + 2
        work_height = browser.execute_script("return window.innerHeight") + 2
        diff_width = width - work_width
        diff_height = height - work_height

        for x, y in zip(window_size_x, window_size_y):
            target_width = x + diff_width
            target_height = y + diff_height

            # Устанавливаем начальные размеры окна
            browser.set_window_size(target_width, target_height)

            # Проверяем размеры
            activ_width = browser.execute_script("return window.innerWidth")
            activ_height = browser.execute_script("return window.innerHeight")

            # Если не совпадает
            if activ_width != x or activ_height != y:
                print(f"Размеры не совпадают. Перезапуск браузера для ({x}, {y})")
                time.sleep(1)
                browser = restart_browser()
                browser.get('https://parsinger.ru/window_size/2/index.html')  # Переход на страницу снова
                browser.set_window_size(target_width, target_height)  # Повторная установка размера
                activ_width = browser.execute_script("return window.innerWidth")
                activ_height = browser.execute_script("return window.innerHeight")
                print(browser.find_element(By.ID, 'result').text)

            # Финальная проверка
            final_width = browser.execute_script("return window.innerWidth")
            final_height = browser.execute_script("return window.innerHeight")
            result = browser.find_element(By.ID, 'result').text
            if result:
                print(f"Result: {result}")

            print(f"Target: ({x}, {y}), Actual: ({final_width}, {final_height})")

    except Exception as e:
        print(f"Ошибка: {e}")
