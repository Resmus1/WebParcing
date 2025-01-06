#  https://stepik.org/lesson/1164757/step/1?unit=1177101


from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless=new")


from selenium import webdriver

# Настройка параметров браузера Chrome для работы в режиме без графического интерфейса (headless)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless=new")  # Включение нового режима headless

# Создание браузера и работа с ним
with webdriver.Chrome(options=chrome_options) as browser:
    try:
        # Открытие веб-страницы с вложенными фреймами
        browser.get("https://demoqa.com/nestedframes")

        # Переключение на первый фрейм с именем "frame1"
        browser.switch_to.frame("frame1")
        # Получение и вывод текста, содержащегося в первом фрейме
        print(browser.find_element("xpath", "//body").text)

        # Переключение на вложенный фрейм внутри "frame1" (по индексу 0)
        browser.switch_to.frame(0)
        # Получение и вывод текста из вложенного фрейма
        print(browser.find_element("xpath", "//body").text)

        # Возврат к родительскому фрейму (frame1)
        browser.switch_to.parent_frame()
        # Снова получение текста из первого фрейма (frame1)
        print(browser.find_element("xpath", "//body").text)

        # Возврат к основному содержимому страницы (выйти из всех фреймов)
        browser.switch_to.default_content()
        print("Default Content")  # Уведомление о возврате к основному контенту
    except Exception as e:
        # Обработка исключений и вывод сообщения об ошибке
        print(f"Error: {e}")
