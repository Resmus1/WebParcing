# https://stepik.org/lesson/732063/step/1?unit=733596

from selenium import webdriver
from selenium.webdriver.common.by import By


options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless=new')
with webdriver.Chrome(options=options_chrome) as browser:
    browser.get('https://parsinger.ru/methods/1/index.html')
    code = browser.find_element(By.ID, 'result').text
    while code == 'refresh page':
        browser.refresh()
        code = browser.find_element(By.ID, 'result').text
        if code != 'refresh page':
            print(code)
