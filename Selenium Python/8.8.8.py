#  https://stepik.org/lesson/732083/step/8?unit=733616

# Импортируем необходимые библиотеки для работы с Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Настройки браузера (включаем режим headless для работы без графического интерфейса)
options = Options()
options.add_argument('--headless=new')

if __name__ == '__main__':
    try:
        # Открываем браузер
        with webdriver.Chrome(options=options) as browser:
            # Загружаем страницу
            browser.get('https://parsinger.ru/selenium/5.9/6/index.html')

            # Находим чекбокс по ID
            check_box = browser.find_element(By.ID, 'myCheckbox')

            # Находим кнопку "Проверить" по тексту
            button = browser.find_element(By.XPATH, "//button[text()='Проверить']")

            # Находим элемент для вывода результата по ID
            result = browser.find_element(By.ID, 'result')

            # Ждем, пока чекбокс станет выбранным (поддерживает состояние selected)
            WebDriverWait(browser, 10).until(EC.element_to_be_selected(check_box))

            # Кликаем по чекбоксу
            check_box.click()

            # Кликаем по кнопке "Проверить"
            button.click()

            # Выводим текст из элемента с результатом
            print(result.text)

    except Exception as e:
        # Обработка ошибок, если что-то пошло не так
        print(f"Alert: {e}")
