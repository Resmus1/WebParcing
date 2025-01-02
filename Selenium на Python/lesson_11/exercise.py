#  https://stepik.org/lesson/1164779/step/1?unit=1177122

# Импортируем необходимые модули из библиотеки Selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Открываем браузер Chrome в контексте менеджера (браузер автоматически закроется после завершения блока with)
with webdriver.Chrome() as browser:
    # Переходим на веб-страницу
    browser.get('https://omayo.blogspot.com/')

    # Создаем объект WebDriverWait с таймаутом 30 секунд и интервалом опроса 0.5 секунды
    wait = WebDriverWait(browser, 30, 0.5)

    # Локаторы для различных элементов на странице
    INVISIBLE_TEXT_AFTER = ('xpath', "//div[@id='deletesuccess']")  # Локатор для элемента, который должен исчезнуть
    VISIBLE_TEXT_AFTER = ('xpath', "//div[@id='delayedText']")      # Локатор для элемента, который должен появиться
    ENABLE_BUTTON = ('xpath', "//input[@id='timerButton']")         # Локатор для кнопки, которая станет активной
    BUTTON_OFF = ('xpath', "//button[text()='Try it']")            # Локатор для кнопки "Try it"
    DISABLE_BUTTON = ('xpath', "//button[@id='myBtn']")            # Локатор для кнопки, которая станет неактивной

    # Ждем, пока элемент с ID 'deletesuccess' станет невидимым (ожидание максимум 25 секунд)
    wait.until(EC.invisibility_of_element(INVISIBLE_TEXT_AFTER), "Alert wait text 25 sec")

    # Ждем, пока элемент с ID 'delayedText' станет видимым (ожидание максимум 10 секунд)
    wait.until(EC.visibility_of_element_located(VISIBLE_TEXT_AFTER), "Alert wait text 10 sec")

    # Ждем, пока кнопка с ID 'timerButton' станет кликабельной (ожидание максимум 30 секунд)
    wait.until(EC.element_to_be_clickable(ENABLE_BUTTON), "Alert wait enable button")

    # Ждем, пока кнопка "Try it" станет кликабельной, и кликаем по ней
    wait.until(EC.element_to_be_clickable(BUTTON_OFF), "Alert click").click()

    # Ждем, пока кнопка с ID 'myBtn' станет неактивной (ожидание максимум 30 секунд)
    wait.until(lambda driver: not driver.find_element(*DISABLE_BUTTON).is_enabled(), "Alert wait disable button")
