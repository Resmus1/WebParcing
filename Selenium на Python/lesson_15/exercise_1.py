#  https://stepik.org/lesson/1164787/step/1?unit=1177130

from selenium import webdriver

# Настройка браузера
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless=new")


def selected_and_checked(browser, dict_buttons):
    """
    Проверяет изменение классов кнопок после клика.

    :param browser: Экземпляр Selenium WebDriver
    :param dict_buttons: Словарь с названиями кнопок и их локаторами
    """
    buttons_dicts = {}

    for num_button, xpath_button in dict_buttons.items():
        buttons_dicts[num_button] = {}

        # Поиск кнопки
        button = browser.find_element(*xpath_button)

        # Получение класса до клика
        buttons_dicts[num_button]['False'] = button.get_attribute('class')

        # Клик по кнопке
        button.click()

        # Получение класса после клика
        buttons_dicts[num_button]['True'] = button.get_attribute('class')

    # Проверка изменений классов кнопок
    for num_button, status_dicts in buttons_dicts.items():
        assert status_dicts['False'] != status_dicts['True'], f"Button '{num_button}' did not change class"
        print(f"Button '{num_button}' class changed successfully.")


# Основной блок выполнения
with webdriver.Chrome(options=chrome_options) as browser:
    try:
        # Открываем тестовую страницу
        browser.get('https://demoqa.com/selectable')

        # Переход на вкладку Grid
        browser.find_element("xpath", "//a[@id='demo-tab-grid']").click()

        # Определяем кнопки для проверки
        buttons = {
            'BUTTON_2': ("xpath", "//li[text()='Two']"),
            'BUTTON_6': ("xpath", "//li[text()='Six']"),
            'BUTTON_7': ("xpath", "//li[text()='Seven']"),
        }

        # Запускаем проверку дважды
        for i in range(2):
            print(f"Step {i + 1}")
            selected_and_checked(browser, buttons)

    except Exception as e:
        print(f"An error occurred: {e}")
