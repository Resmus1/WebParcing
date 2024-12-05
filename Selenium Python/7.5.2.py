#  https://parsinger.ru/selenium/5.8/2/index.html

from selenium import webdriver
from selenium.webdriver.common.by import By

# Главная точка входа программы
if __name__ == '__main__':
    try:
        # Запускаем браузер Chrome с использованием WebDriver
        with webdriver.Chrome() as browser:
            # Открываем нужную страницу
            browser.get('https://parsinger.ru/selenium/5.8/2/index.html')

            # Находим все кнопки на странице с помощью класса 'buttons'
            all_buttons = browser.find_elements(By.CLASS_NAME, 'buttons')
            # Находим поле ввода кода на странице
            input_area = browser.find_element(By.ID, 'input')
            # Находим кнопку проверки
            check_button = browser.find_element(By.ID, 'check')

            # Перебираем все найденные кнопки
            for button in all_buttons:
                # Нажимаем на каждую кнопку
                button.click()

                # Обрабатываем всплывающее окно (alert)
                alert = browser.switch_to.alert
                num_alert = alert.text
                alert.accept()

                # Вводим код и нажимаем проверку
                input_area.send_keys(num_alert)
                check_button.click()

                # Находим результат и если он верный выводим его в терминал
                result = browser.find_element(By.ID, 'result').text
                if result != 'Неверный пин-код':
                    print(result)

    # Обрабатываем любые ошибки, которые могут возникнуть в процессе выполнения программы
    except Exception as e:
        # Выводим сообщение об ошибке в терминал
        print(f"Ошибка: {e}")
