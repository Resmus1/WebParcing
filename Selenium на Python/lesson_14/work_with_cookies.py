#  https://stepik.org/lesson/1164784/step/1?unit=1177127

import os
import pickle
import time

from selenium import webdriver

# Открываем браузер Chrome с использованием контекстного менеджера
with webdriver.Chrome() as browser:
    # Переходим на страницу авторизации
    browser.get('https://www.freeconferencecall.com/ru/kz/login')

    # Локаторы для элементов страницы (логин, пароль и кнопка входа)
    LOGIN_FIELD = ('xpath', "//input[@id='login_email']")  # Поле ввода логина
    PASSWORD_FIELD = ('xpath', "//input[@id='password']")  # Поле ввода пароля
    SUBMIT_BUTTON = ('xpath', "//button[@id='loginformsubmit']")  # Кнопка отправки формы

    time.sleep(3)  # Ждем загрузки страницы (нежелательно использовать sleep, лучше явное ожидание)

    # Заполняем форму авторизации
    browser.find_element(*LOGIN_FIELD).send_keys('elbandito237@gmail.com')  # Вводим логин
    browser.find_element(*PASSWORD_FIELD).send_keys('123456789S')  # Вводим пароль
    browser.find_element(*SUBMIT_BUTTON).click()  # Нажимаем кнопку "Войти"

    time.sleep(3)  # Ждем завершения авторизации

    # Сохраняем куки авторизованной сессии в файл cookies.pkl
    pickle.dump(browser.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl", "wb"))

    # Удаляем все куки из текущей сессии, чтобы проверить их восстановление
    browser.delete_all_cookies()
    browser.refresh()  # Обновляем страницу после удаления куки
    browser.delete_all_cookies()  # Повторное удаление для убедительности

    time.sleep(3)  # Ждем завершения операции удаления

    # Загружаем ранее сохраненные куки из файла
    cookies = pickle.load(open(os.getcwd() + "/cookies/cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)  # Добавляем каждый куки в текущую сессию

    browser.refresh()  # Обновляем страницу, чтобы применились загруженные куки
    time.sleep(3)  # Ждем завершения загрузки страницы после применения куки
