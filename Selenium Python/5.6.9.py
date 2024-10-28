# https://stepik.org/lesson/732063/step/10?unit=733596

# Импортируем необходимые модули из библиотеки Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем объект настроек для Chrome
options_chrome = webdriver.ChromeOptions()
# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome.add_argument('--headless=new')

# Открываем браузер Chrome с заданными настройками и работаем с ним в блоке 'with'
with webdriver.Chrome(options=options_chrome) as browser:
    # Загружаем веб-страницу по указанному URL
    browser.get('https://parsinger.ru/selenium/5.5/4/1.html')

    # Находим все элементы с классом 'parent' на странице
    elements = browser.find_elements(By.CLASS_NAME, 'parent')

    # Проходим по каждому элементу (блоку) в списке
    for box in elements:
        # Извлекаем текст из <textarea> с атрибутом color="gray"
        num = box.find_element(By.CSS_SELECTOR, 'textarea[color="gray"]').text
        # Очищаем содержимое <textarea> с атрибутом color="gray"
        box.find_element(By.CSS_SELECTOR, 'textarea[color="gray"]').clear()
        # Вставляем извлеченный текст в <textarea> с атрибутом color="blue"
        box.find_element(By.CSS_SELECTOR, 'textarea[color="blue"]').send_keys(num)
        # Нажимаем на кнопку внутри текущего блока
        box.find_element(By.TAG_NAME, 'button').click()

    # Нажимаем на кнопку с ID 'checkAll' после обработки всех блоков
    browser.find_element(By.ID, 'checkAll').click()

    # Выводим текст элемента с ID 'congrats'
    print(browser.find_element(By.ID, 'congrats').text)
