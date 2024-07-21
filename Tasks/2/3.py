# https://stepik.org/lesson/732063/step/3?unit=733596

from selenium import webdriver

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless=new')
with webdriver.Chrome(options=options_chrome) as browser:
    browser.get('https://parsinger.ru/methods/3/index.html')
    cookies = browser.get_cookies()
    sum_cookies = 0
    for dict_key in cookies:
        if int(dict_key['name'].rsplit('_', 1)[-1]) % 2 == 0:
            sum_cookies += int(dict_key['value'])
    print(sum_cookies)
