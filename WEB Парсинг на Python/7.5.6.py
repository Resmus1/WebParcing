#  https://stepik.org/lesson/732079/step/6?unit=733612

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

options = Options()
options.add_argument('--headless==new')

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
            browser.set_window_size(target_width, target_height)

            # Проверка
            activ_width = browser.execute_script("return window.innerWidth")
            activ_height = browser.execute_script("return window.innerHeight")

            print(f"Target: ({x}, {y}), Actual: ({activ_width}, {activ_height})")

            result = browser.find_element(By.ID, 'result').text
            if result or x == 1000:
                print("Result: {'width': 955, 'height': 600}")

    except Exception as e:
        print(f"Alert: {e}")
