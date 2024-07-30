# https://stepik.org/lesson/732063/step/9?unit=733596

from selenium import webdriver
from selenium.webdriver.common.by import By


options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless=new')
with webdriver.Chrome(options=options_chrome) as browser:
    browser.get('https://parsinger.ru/selenium/5.5/4/1.html')
    elements = browser.find_elements(By.CLASS_NAME, 'parent')
    for box in elements:
        num = box.find_element(By.CSS_SELECTOR, 'textarea[color="gray"]').text
        box.find_element(By.CSS_SELECTOR, 'textarea[color="gray"]').clear()
        box.find_element(By.CSS_SELECTOR, 'textarea[color="blue"').send_keys(num)
        box.find_element(By.TAG_NAME, 'button').click()
    browser.find_element(By.ID, 'checkAll').click()
    print(browser.find_element(By.ID, 'congrats').text)
