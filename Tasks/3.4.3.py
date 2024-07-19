# https://stepik.org/lesson/731861/step/4?unit=733396

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')
    input_form = browser.find_elements(By.CLASS_NAME, 'form')
    for i in input_form:
        i.send_keys('Текст')
    browser.find_element(By.ID, 'btn').click()
    print(browser.find_element(By.ID, 'result').text)
