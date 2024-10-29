# https://stepik.org/lesson/732069/step/1?unit=733602


from selenium import webdriver
from selenium.webdriver.common.by import By

# Настройки для браузера Chrome
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless=new')  # Запускаем браузер в фоновом режиме (без GUI)

# Используем контекстный менеджер для открытия браузера
with webdriver.Chrome(options=options_chrome) as browser:
    # Переходим на целевую страницу
    browser.get('https://parsinger.ru/scroll/2/index.html')
    sum_num = 0

    # Находим все блоки с классом 'item'
    all_blocks = browser.find_elements(By.CLASS_NAME, 'item')
    for block in all_blocks:
        # Кликаем по чекбоксу внутри блока
        checkbox = block.find_element(By.CLASS_NAME, 'checkbox_class')
        checkbox.click()

        # Получаем текст из <span> внутри блока и суммируем
        span_text = block.find_element(By.TAG_NAME, 'span').text
        if span_text:
            sum_num += int(span_text)

    print(sum_num)
