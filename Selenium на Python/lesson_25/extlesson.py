#  https://stepik.org/lesson/1366598/step/1?unit=1382605

import time

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_extension("./extensions/adblock.crx")

with webdriver.Chrome(options=chrome_options) as browser:
    try:
        browser.get("https://test.adminforge.de/adblock.html")
        time.sleep(5)
    except Exception as e:
        print(f"ERROR: {e}")
