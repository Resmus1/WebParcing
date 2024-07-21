import time
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('user-data-dir=C:\\Users\\Re$mus\\AppData\\Local\\Google\\Chrome\\User Data')
options_chrome.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')
options_chrome.add_argument('--hidden')
with webdriver.Chrome(options=options_chrome) as browser:
    browser.get('https://yandex.ru/search/?text=%D0%BA%D0%B0%D0%B1%D0%B0%D0%BD&lr=24&redircnt=1721555632.1')
    time.sleep(10)
    for _ in range(10):
        browser.find_element(By.CLASS_NAME,'Button2 Button2_pin_circle-circle EasterEggFab-Button EasterEggControls-Control EasterEggControls-Control_type_fab').click()
        time.sleep(1)
    time.sleep(10)
