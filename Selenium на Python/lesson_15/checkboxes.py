#  https://stepik.org/lesson/1164786/step/1?unit=1177129

from selenium import webdriver

# Настраиваем опции для браузера
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless=new")  # Указываем режим headless для работы без графического интерфейса

# Запускаем браузер в контексте менеджера
with webdriver.Chrome(options=chrome_options) as browser:
    # Открываем целевую страницу с чекбоксами
    browser.get("https://the-internet.herokuapp.com/checkboxes")

    # Определяем локаторы для двух чекбоксов
    CHECKBOX_1 = ("xpath", "(//input[@type='checkbox'])[1]")  # Первый чекбокс
    CHECKBOX_2 = ("xpath", "(//input[@type='checkbox'])[2]")  # Второй чекбокс

    # Работа с первым чекбоксом
    checkbox_1 = browser.find_element(*CHECKBOX_1)  # Находим первый чекбокс
    checkbox_1.click()  # Переключаем состояние чекбокса (если он включён, выключится, и наоборот)
    status_checkbox_1 = checkbox_1.get_attribute("checked")  # Получаем атрибут "checked" (None, если чекбокс выключен)

    # Работа со вторым чекбоксом
    checkbox_2 = browser.find_element(*CHECKBOX_2)  # Находим второй чекбокс
    checkbox_2.click()  # Переключаем состояние чекбокса
    status_checkbox_2 = checkbox_2.is_selected()  # Проверяем, выбран ли чекбокс (возвращает True/False)

    # Проверяем состояние первого чекбокса
    assert status_checkbox_1 is not None, "CheckBox is False"  # Убеждаемся, что он установлен

    # Проверяем состояние второго чекбокса
    assert status_checkbox_2 is False, "CheckBox is True"  # Проверяем, что он не установлен (ошибка в текущей логике)

    # Если проверки прошли успешно, выводим результаты
    print("Selected checkbox")  # Сообщение, если первый чекбокс был успешно выбран
    print("Unselected checkbox")  # Сообщение, если второй чекбокс был успешно выключен

