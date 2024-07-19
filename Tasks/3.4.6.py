# https://stepik.org/lesson/731861/step/7?unit=733396

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/3/3.html')
    divs = browser.find_elements(By.CLASS_NAME, 'text')
    p_sum = 0
    for div in divs:
        p_sum += int(div.find_element(By.XPATH, './p[2]').text)
    print(p_sum)