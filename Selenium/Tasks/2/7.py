# https://stepik.org/lesson/732063/step/8?unit=733596

from selenium import webdriver
from selenium.webdriver.common.by import By


options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless=new')
with webdriver.Chrome(options=options_chrome) as browser:
    browser.get('https://parsinger.ru/selenium/5.5/3/1.html')
    elements = browser.find_elements(By.CLASS_NAME, 'parent')
    result_sum = 0
    for box in elements:
        if box.find_element(By.CLASS_NAME, 'checkbox').is_selected():
            result_sum += int(box.find_element(By.TAG_NAME, 'textarea').text)
    print(result_sum)
