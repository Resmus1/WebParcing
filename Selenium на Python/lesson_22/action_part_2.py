#  https://stepik.org/lesson/1164768/step/1?unit=1177112
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Настройки для запуска браузера Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна браузера

# Локаторы для элементов на странице
SOURCE_LOCATOR = ("xpath", "//div[@id='draggable']")  # Элемент, который нужно перетащить (первая страница)
TARGET_LOCATOR = ("xpath", "//div[@id='droppable']")  # Целевая зона для элемента (первая страница)
SOURCE_2_LOCATOR = ("xpath", "//div[@class='grid__item'][4]")  # Элемент, который нужно перетащить (вторая страница)
TARGET_2_LOCATOR = ("xpath", "//div[@class='drop-area__item'][2]")  # Целевая зона для элемента (вторая страница)

# Открытие браузера и выполнение действий
with webdriver.Chrome(options=chrome_options) as browser:
    # Инициализация ActionChains для выполнения сложных действий
    action = ActionChains(browser)

    try:
        # Переход на первую страницу для выполнения drag-and-drop
        browser.get("https://demoqa.com/droppable")

        # Поиск элементов для перетаскивания
        sourcer = browser.find_element(*SOURCE_LOCATOR)  # Исходный элемент для перетаскивания
        target = browser.find_element(*TARGET_LOCATOR)  # Целевая зона для перетаскивания

        # Выполнение drag-and-drop на первой странице
        action.drag_and_drop(sourcer, target).pause(2).perform()

        # Переход на вторую страницу для выполнения drag-and-drop
        browser.get("https://tympanus.net/Development/DragDropInteractions/index.html")

        # Поиск элементов для перетаскивания
        sourcer_2 = browser.find_element(*SOURCE_2_LOCATOR)  # Исходный элемент для перетаскивания
        target_2 = browser.find_element(*TARGET_2_LOCATOR)  # Целевая зона для перетаскивания

        # Выполнение drag-and-drop через ручное управление мышью
        action.click_and_hold(sourcer_2).pause(2).move_to_element(target_2).release().pause(2).perform()

    except Exception as e:
        # Обработка исключений и вывод ошибки
        print(f"ERROR: {e}")
