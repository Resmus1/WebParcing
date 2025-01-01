#  https://stepik.org/lesson/1166698/step/3?unit=1179022

from selenium import webdriver  # Импортируем Selenium WebDriver для управления браузером
from selenium.webdriver.chrome.options import Options  # Импортируем настройки для Chrome
from selenium.webdriver.support import expected_conditions as EC  # Импортируем условия для ожидания
from selenium.webdriver.support.ui import WebDriverWait  # Импортируем механизм явного ожидания

# Настройки для Chrome браузера
options = Options()
options.add_argument('--headless=new')  # Запуск браузера в headless режиме (без интерфейса)

# Создание экземпляра браузера с настройками
with webdriver.Chrome(options=options) as browser:
    # Открытие целевой страницы
    browser.get('https://testautomationpractice.blogspot.com/')

    # Ожидание элемента с классом 'wikipedia-icon' на странице
    # Этот элемент может быть иконкой или логотипом Wikipedia
    wiki_icon = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located(('class name', 'wikipedia-icon'))
    )

    # Ожидание поля ввода для поиска с ID 'Wikipedia1_wikipedia-search-input'
    # Это поле используется для ввода поискового запроса
    wiki_search = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located(('id', 'Wikipedia1_wikipedia-search-input'))
    )

    # Ожидание кнопки поиска Wikipedia с классом 'wikipedia-search-button'
    # Это кнопка, которая запускает поиск на сайте
    wiki_search_button = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located(('class name', 'wikipedia-search-button'))
    )

    # Ожидание загрузки всех элементов <div> на странице
    divs = WebDriverWait(browser, 30).until(  # Мы ожидаем загрузки всех элементов <div>
        EC.presence_of_all_elements_located(('tag name', 'div'))  # Ищем элементы с тегом <div>
    )

    # Доступ к 5-му элементу списка (индексация с 0, поэтому divs[4] - это 5-й элемент)
    element = divs[4]

    # Печать найденных элементов на странице
    print(wiki_icon, wiki_search, wiki_search_button, element, sep='\n')
