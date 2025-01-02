# Импортируем модуль webdriver из библиотеки Selenium

from selenium import webdriver

# Создаем экземпляр браузера Chrome, который будет автоматически закрываться после выполнения блока with
with webdriver.Chrome() as browser:
    # Устанавливаем неявное ожидание в 10 секунд (элементы будут искаться до 10 секунд перед тем, как выбросить исключение)
    browser.implicitly_wait(10)

    # Открываем веб-страницу по указанному URL
    browser.get('https://demoqa.com/dynamic-properties')

    # Находим кнопку на странице по XPath. Кнопка имеет атрибут id='visibleAfter'
    button = browser.find_element('xpath', "//button[@id='visibleAfter']")

    # Кликаем на найденную кнопку
    button.click()
