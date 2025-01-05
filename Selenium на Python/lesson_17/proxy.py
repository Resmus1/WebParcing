#  https://stepik.org/lesson/1164790/step/1?unit=1177133

import time

from selenium import webdriver

PROXY_SERVER = "128.140.113.110:8081"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--proxy-server={PROXY_SERVER}")

with webdriver.Chrome(options=chrome_options) as browser:
    try:
        browser.get("https://2ip.ru/")

        time.sleep(5)
    except Exception as e:
        print(f"ERROR: {e}")
