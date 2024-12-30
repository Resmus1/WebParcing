#  https://stepik.org/lesson/732083/step/9?unit=733616

# Импортируем необходимые библиотеки для работы с Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Настройки для браузера Chrome (режим headless для работы без графического интерфейса)
options = Options()
options.add_argument('--headless=new')

if __name__ == '__main__':
    try:
        # Открытие браузера с использованием контекстного менеджера
        with webdriver.Chrome(options=options) as browser:
            # Переход на целевую веб-страницу
            browser.get('https://parsinger.ru/selenium/5.9/7/index.html')

            # Находим элемент для вывода результата по ID
            result = browser.find_element(By.ID, 'result')

            # Поиск всех элементов с классом "container" (обертка для чекбокса и кнопки)
            containers = browser.find_elements(By.CLASS_NAME, 'container')

            # Итерация по каждому найденному контейнеру
            for container in containers:
                # Поиск чекбокса внутри текущего контейнера
                check_box = container.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')

                # Поиск кнопки "Проверить" внутри текущего контейнера
                button = container.find_element(By.XPATH, ".//button[text()='Проверить']")

                # Ожидание, пока чекбокс будет отмечен (элемент выбран)
                WebDriverWait(browser, 10).until(EC.element_to_be_selected(check_box))

                # Клик по кнопке "Проверить"
                button.click()
            # Выводим текст из элемента с результатом
            print(result.text)

    # Обработка исключений, если возникают ошибки во время выполнения
    except Exception as e:
        print(f"Alert: {e}")
