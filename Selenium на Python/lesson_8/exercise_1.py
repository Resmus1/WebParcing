from selenium import webdriver  # Импортируем WebDriver для управления браузером.
from selenium.webdriver.chrome.options import Options  # Импортируем класс для настройки браузера.

# Создаем объект настроек для ChromeDriver.
options = Options()
# Добавляем аргумент '--headless=new', чтобы запустить браузер в безголовом режиме (без графического интерфейса).
options.add_argument('--headless=new')

# Используем контекстный менеджер для автоматического закрытия браузера по завершению работы.
with webdriver.Chrome(options=options) as browser:
    # Загружаем веб-страницу по указанному URL.
    browser.get('https://demoqa.com/text-box')

    # Находим элементы формы по XPath:
    # Поле ввода для имени пользователя.
    user_name = browser.find_element('xpath', "//input[@id='userName']")
    # Поле ввода для email.
    email = browser.find_element('xpath', "//input[@id='userEmail']")
    # Поле для ввода текущего адреса.
    current_address = browser.find_element('xpath', "//textarea[@id='currentAddress']")
    # Поле для ввода постоянного адреса.
    permanent_address = browser.find_element('xpath', "//textarea[@id='permanentAddress']")

    # Вводим тестовые данные в соответствующие поля формы:
    user_name.send_keys('Ivan')
    email.send_keys('ivan@mail.com')
    current_address.send_keys('Ivanovskaya 7')
    permanent_address.send_keys('Testovaia 8')

    # Проверка, что введенные данные правильно отобразились в полях:
    # Проверяем, что значение в поле ввода имени соответствует 'Ivan'.
    assert user_name.get_attribute('value') == 'Ivan', 'Alert input Name'
    # Проверяем, что значение в поле ввода email соответствует 'ivan@mail.com'.
    assert email.get_attribute('value') == 'ivan@mail.com', 'Alert input email'
    # Проверяем, что значение в поле ввода текущего адреса соответствует 'Ivanovskaya 7'.
    assert current_address.get_attribute('value') == 'Ivanovskaya 7', 'Alert input current_address'
    # Проверяем, что значение в поле ввода постоянного адреса соответствует 'Testovaia 8'.
    assert permanent_address.get_attribute('value') == 'Testovaia 8', 'Alert input permanent address'
