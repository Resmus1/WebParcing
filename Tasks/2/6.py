# https://stepik.org/lesson/732063/step/7?unit=733596

from selenium import webdriver
from selenium.webdriver.common.by import By


options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless=new')
with webdriver.Chrome(options=options_chrome) as browser:
    browser.get('https://parsinger.ru/scroll/4/index.html')
    elements = browser.find_elements(By.CLASS_NAME, 'btn')
    result_sum = 0
    for btn in elements:
        browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
        btn.click()
        result_sum += int(browser.find_element(By.ID, 'result').text)
    print(result_sum)
