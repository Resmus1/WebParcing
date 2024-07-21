# https://stepik.org/lesson/731861/step/11?unit=733396

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.html')
    ex = eval(browser.find_element(By.ID, 'text_box').text)
    l_num = browser.find_elements(By.TAG_NAME, 'option')
    for num in l_num:
        if int(num.text) == ex:
            num.click()
            browser.find_element(By.CLASS_NAME, 'btn').click()
            print(browser.find_element(By.ID, 'result').text)
            break
