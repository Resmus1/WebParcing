#  https://stepik.org/lesson/897512/step/13?unit=1066949

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless=new')

try:
    with webdriver.Chrome(options=options) as browser:
        browser.get('https://parsinger.ru/selenium/5.10/6/index.html')

        sliders = browser.find_elements(By.CLASS_NAME, 'slider-container')
        result = browser.find_element(By.ID, 'message')

        for slider in sliders:
            slider_dot = slider.find_element(By.CLASS_NAME, 'volume-slider')
            current_value = slider.find_element(By.CLASS_NAME, 'current-value')
            target_value = slider.find_element(By.CLASS_NAME, 'target-value')
            current_value_int = int(current_value.text)
            target_value_int = int(target_value.text)

            if current_value_int > target_value_int:
                while current_value_int != target_value_int:
                    slider_dot.send_keys(Keys.ARROW_LEFT)
                    current_value_int = int(current_value.text)

            elif current_value_int < target_value_int:
                while current_value_int != target_value_int:
                    slider_dot.send_keys(Keys.ARROW_RIGHT)
                    current_value_int = int(current_value.text)
        print(result.text)
except Exception as e:
    print(f"Alert: {e}")
