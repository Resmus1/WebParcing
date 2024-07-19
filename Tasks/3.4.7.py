# https://stepik.org/lesson/731861/step/8?unit=733396

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/4/4.html')
    check_box = browser.find_elements(By.CLASS_NAME, 'check')
    for check in check_box:
        check.click()
    browser.find_element(By.CLASS_NAME, 'btn').click()
    print(browser.find_element(By.ID, 'result').text)
