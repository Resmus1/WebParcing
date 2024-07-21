# https://stepik.org/lesson/731861/step/10?unit=733396

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.html')
    l_num = browser.find_elements(By.TAG_NAME, 'option')
    sum_num = 0
    for num in l_num:
        sum_num += int(num.text)
    browser.find_element(By.ID, 'input_result').send_keys(str(sum_num))
    browser.find_element(By.CLASS_NAME, 'btn').click()
    print(browser.find_element(By.ID, 'result').text)
