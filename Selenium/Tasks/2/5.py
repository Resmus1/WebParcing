# https://stepik.org/lesson/732063/step/5?unit=733596

from selenium import webdriver
from selenium.webdriver.common.by import By


options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless=new')
with webdriver.Chrome(options=options_chrome) as browser:
    browser.get('https://parsinger.ru/methods/5/index.html')
    l_href = [item.get_attribute('href') for item in browser.find_elements(By.TAG_NAME, 'a')]
    expiry = 0
    result = 0
    for link in l_href:
        browser.get(link)
        cookies = browser.get_cookies()
        for key in cookies:
            if key['expiry'] > expiry:
                result = browser.find_element(By.ID, 'result').text
                expiry = key['expiry']
    print(result)
