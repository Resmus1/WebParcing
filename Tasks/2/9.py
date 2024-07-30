# https://stepik.org/lesson/732063/step/10?unit=733596

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless=new')
with webdriver.Chrome(options=options_chrome) as browser:
    browser.get('https://parsinger.ru/selenium/5.5/5/1.html')
    parent_boxes = browser.find_elements(By.XPATH, '//div[@id="main-container"]/div')
    for parent_box in parent_boxes:
        color = parent_box.find_element(By.XPATH, './/span').text
        select = Select(parent_box.find_element(By.XPATH, './/select'))
        select.select_by_value(color)
        parent_box.find_element(By.XPATH, f'.//button[@data-hex="{color}"]').click()
        parent_box.find_element(By.XPATH, './/input[@type="checkbox"]').click()
        parent_box.find_element(By.XPATH, './/input[@type="text"]').send_keys(color)
        parent_box.find_element(By.XPATH, './/button[text()="Проверить"]').click()
    browser.find_element(By.XPATH, '//button[text()="Проверить все элементы"]').click()
    print(browser.switch_to.alert.text)
