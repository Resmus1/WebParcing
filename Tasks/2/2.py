from selenium import webdriver
from selenium.webdriver.common.by import By

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless=new')
with webdriver.Chrome(options=options_chrome) as browser:
    browser.get('https://parsinger.ru/selenium/5.5/1/1.html')
    elements = browser.find_elements(By.CLASS_NAME, 'text-field')
    for field in elements:
        field.clear()
    browser.find_element(By.ID,'checkButton').click()
    print(browser.switch_to.alert.text)
