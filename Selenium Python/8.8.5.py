#  https://stepik.org/lesson/732083/step/5?unit=733616

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Настройка опций для браузера Chrome
options = Options()
# Запуск браузера в режиме headless (без графического интерфейса)
options.add_argument('--headless=new')

# Список ID элементов, которые нужно найти и кликнуть
ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I',
               'jolHZqD1', 'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']

# Главная точка входа в программу
if __name__ == '__main__':
    try:
        # Инициализация браузера с использованием контекстного менеджера (автоматически закроется)
        with webdriver.Chrome(options=options) as browser:
            # Открытие заданной страницы
            browser.get('https://parsinger.ru/selenium/5.9/3/index.html')

            # Цикл по всем ID из списка
            for i in ids_to_find:
                # Ожидание видимости элемента с данным ID и его клик
                WebDriverWait(browser, 30, poll_frequency=0.1).until(  # Установка времени ожидания 30 секунд
                    EC.visibility_of_element_located((By.ID, i))  # Условие: элемент видим на странице
                ).click()  # Клик по элементу

            # Переключение на всплывающее окно (alert) и вывод его текста
            print(browser.switch_to.alert.text)

    except Exception as e:
        # Обработка ошибок и вывод их описания в случае исключения
        print(f'Alert: {e}')
