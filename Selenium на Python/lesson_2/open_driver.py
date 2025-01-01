#  https://stepik.org/lesson/1140235/step/1?unit=1151908

from selenium import webdriver

try:
    with webdriver.Chrome() as browser:
        browser.get('https://www.google.com/')

except Exception as e:
    print(e)