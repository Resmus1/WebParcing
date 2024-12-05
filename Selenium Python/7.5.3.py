#  https://stepik.org/lesson/732079/step/3?unit=733612

from selenium import webdriver
from selenium.webdriver.common.by import By

# Главная точка входа программы
if __name__ == '__main__':
    try:
        # Запускаем браузер Chrome с использованием WebDriver
        with webdriver.Chrome() as browser:
            # Открываем нужную страницу
            browser.get('https://parsinger.ru/selenium/5.8/3/index.html')

            # Находим все пин-коды
            pincode = browser.find_elements(By.CLASS_NAME, 'pin')
            # Находим кнопку проверки
            check_button = browser.find_element(By.ID, 'check')

            # Перебираем все найденные пин-коды
            for pin in pincode:
                # Извлекаем текст из pin
                extract = pin.text

                # Вызываем окно ввода
                check_button.click()
                enter_field = browser.switch_to.alert

                # Отправляем PIN
                enter_field.send_keys(extract)
                enter_field.accept()

                # Проверяем результат
                result = browser.find_element(By.ID, 'result').text
                if result != 'Неверный пин-код':
                    print(result)

    # Обрабатываем любые ошибки, которые могут возникнуть в процессе выполнения программы
    except Exception as e:
        # Выводим сообщение об ошибке в терминал
        print(f"Ошибка: {e}")
