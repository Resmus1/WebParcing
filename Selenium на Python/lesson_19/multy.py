#  https://stepik.org/lesson/1164792/step/1?unit=1177135
import time

from selenium import webdriver

# Создание и настройка опций для браузера (например, размер окна)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

# Определение локаторов для полей ввода и кнопки
LOGIN_FIELD = ("xpath", "//input[@type='email']")  # Поле для ввода email
PASSWORD_FIELD = ("xpath", "//input[@type='password']")  # Поле для ввода пароля
SUBMIT_BUTTON = ("xpath", "//button[@class='btn btn-primary btn-block !p-2']")  # Кнопка отправки формы

# Открытие браузера для первого пользователя
with webdriver.Chrome() as user_1:
    try:
        # Переход на страницу входа
        user_1.get("https://hyperskill.org/login")

        # Находим поле для ввода email и вводим данные
        user_1.find_element(*LOGIN_FIELD).send_keys('TEST USER')

        # Находим поле для ввода пароля и вводим данные
        user_1.find_element(*PASSWORD_FIELD).send_keys('TEST PASSWORD')

        # Нажимаем на кнопку "Войти"
        user_1.find_element(*SUBMIT_BUTTON).click()

        # Добавляем небольшую задержку, чтобы убедиться, что действия завершены
        time.sleep(3)
    except Exception as e:
        # В случае ошибки печатаем её в консоль (но исключение не прерывает выполнение)
        pass
        print(f"ERROR User_1: {e}")

# Открытие браузера для второго пользователя
with webdriver.Chrome() as user_2:
    try:
        # Переход на страницу входа
        user_2.get("https://hyperskill.org/login")

        # Добавляем задержку, чтобы страница успела загрузиться
        time.sleep(3)
    except Exception as a:
        # В случае ошибки печатаем её в консоль (но исключение не прерывает выполнение)
        pass
        print(f"ERROR User_2: {a}")
