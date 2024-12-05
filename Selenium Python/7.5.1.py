#  https://stepik.org/lesson/732079/step/1?unit=733612

from selenium import webdriver
from selenium.webdriver.common.by import By

# Главная точка входа программы
if __name__ == "__main__":
    try:
        # Запускаем браузер Chrome с использованием WebDriver
        with webdriver.Chrome() as browser:
            # Открываем нужную страницу
            browser.get('https://parsinger.ru/selenium/5.8/1/index.html')

            # Находим все кнопки на странице с помощью класса 'buttons'
            all_buttons = browser.find_elements(By.CLASS_NAME, 'buttons')

            # Перебираем все найденные кнопки
            for button in all_buttons:
                # Нажимаем на каждую кнопку
                button.click()

                # Пытаемся обработать всплывающее окно (alert)
                alert = browser.switch_to.alert
                # Принудительно принимаем предупреждение (закрываем его)
                alert.accept()

                # Получаем текст из элемента с ID 'result'
                result = browser.find_element(By.ID, 'result').text

                # Если текст в элементе найден (не пустой), выводим его
                if result:
                    print(result)  # Выводим результат в терминал
                    break  # Прерываем цикл, так как код найден

    # Обрабатываем любые ошибки, которые могут возникнуть в процессе выполнения программы
    except Exception as e:
        # Выводим сообщение об ошибке в терминал
        print(f"Ошибка: {e}")
