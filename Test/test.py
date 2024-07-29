import time
from selenium import webdriver


with webdriver.Chrome() as driver:
    driver.get("https://stepik.org/course/104774")
    time.sleep(5)