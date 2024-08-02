# https://stepik.org/lesson/731861/step/6?unit=733396

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/3/3.html')
    all_nums = browser.find_elements(By.TAG_NAME, 'p')
    num_sum = 0
    for num in all_nums:
        num_sum += int(num.text)
    print(num_sum)
    