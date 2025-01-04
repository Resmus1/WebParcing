#  https://stepik.org/lesson/1164785/step/1?unit=1177128

import time
import os
import pickle

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)

with webdriver.Chrome(options=chrome_options) as browser:
    wait = WebDriverWait(browser, 30, 0.5)

    browser.get(
        "https://ozon.kz/product/notebook-noutbuk-15-6-ram-16-gb-ssd-512-gb-amd-radeon-windows-pro-seryy-russkaya-raskladka-1224886064/?advert=ACIBT-AsD72ip7vDDXAq5mFqYudlfP8BqFyhuNfikuTYnmniuH25JK-K_J6R-1tKpQZgr9lZpTRYZc1y4pDXmNGlQypw-OekF_W02kG_QO-tuW5e6Nl6f_F7s1PlqPxAwWdgvDmBPEYW2TDrded2PnsMAKaplmWDRNNUqvWNry1PztA5uVEzTGtLtSP1yrXsn1_TjdKVIhlS2ppsM2xOqDHYbepyuFx7aX85Bf33Rh75mGpiYPl6iiQonjKyatdQQVcOcO57uz6rP3vYGYCunD2W5BZ_MACy5PldimI2hsQ_KMmYf3DryAEJeS5i08F-u7LUwFLHfQxVjjmWLAEv1Qo5kYdQdRnPjHEBrazhTqLmKNNN48cqA4OgJIhqeC3YEC8XRccp3L6Gww&avtc=1&avte=4&avts=1735980766"
    )

    ADD_BUTTON = ("xpath", "(//button[@class='jy8_27 b2121-a0 b2121-b2 b2121-a4'])[1]")
    INDICATOR = ("xpath", "//span[text()='1'][1]")
    CART = ("xpath", "//a[@data-widget='headerIcon']")

    wait.until(EC.element_to_be_clickable(ADD_BUTTON)).click(), "Add in cart Doesn't work"
    wait.until(EC.element_to_be_clickable(INDICATOR), 'Indicator no change')
    wait.until(EC.element_to_be_clickable(CART)).click(), "Cart Doesn't work"

    pickle.dump(browser.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl", "wb"))

    time.sleep(5)

    browser.delete_all_cookies()
    browser.refresh()
    time.sleep(5)

    cookies = pickle.load(open(os.getcwd() + "/cookies/cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.refresh()
    time.sleep(5)
