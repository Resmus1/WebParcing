# https://stepik.org/lesson/732063/step/11?unit=733596

from selenium import webdriver


optons_chrome = webdriver.ChromeOptions()
optons_chrome.add_argument('--headless=new')
with webdriver.Chrome(options=optons_chrome) as browser:
    browser.get('https://parsinger.ru/methods/3/index.html')
    cookies = browser.get_cookies()
    sum_cookie = 0
    for cookie in cookies:
        sum_cookie += int(cookie['value'])
    print(sum_cookie)
