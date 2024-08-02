# https://stepik.org/lesson/732063/step/4?unit=733596

from selenium import webdriver
from selenium.webdriver.common.by import By


options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless=new')
with webdriver.Chrome(options=options_chrome) as browser:
    browser.get('https://parsinger.ru/selenium/5.5/2/1.html')
    fields = browser.find_elements(By.XPATH, '//*[@data-enabled="true"]')
    for fil in fields:
        fil.clear()
    browser.find_element(By.ID, 'checkButton').click()
    print(browser.switch_to.alert.text)
