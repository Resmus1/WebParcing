#  https://stepik.org/lesson/732079/step/8?unit=733612

# Импортируем WebDriver для взаимодействия с веб-браузером
from selenium import webdriver
# Импортируем Options для настройки браузера
from selenium.webdriver.chrome.options import Options
# Импортируем локаторы для поиска элементов на странице
from selenium.webdriver.common.by import By

# Список URL-адресов для взаимодействия
sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html',
         'http://parsinger.ru/blank/1/3.html', 'http://parsinger.ru/blank/1/4.html',
         'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html']

# Настройки для браузера Chrome
options = Options()
# Запускаем браузер в фоновом режиме (без графического интерфейса)
options.add_argument('--headless==new')

if __name__ == '__main__':
    # Переменная для хранения суммы чисел
    sum_nums = 0
    try:
        # Инициализируем экземпляр браузера Chrome
        browser = webdriver.Chrome(options=options)
        # Проходим по каждому URL в списке
        for site in sites:
            # Открываем новый таб с текущим URL
            browser.execute_script(f"window.open('{site}')")
            # Переходим на страницу по указанному URL
            browser.get(site)
            # Кликаем на чекбокс с указанным классом
            browser.find_element(By.CLASS_NAME, 'checkbox_class').click()
            # Берем текст из элемента с ID "result" и вычисляем квадратный корень
            num = int(browser.find_element(By.ID, 'result').text) ** 0.5
            # Добавляем результат к общей сумме
            sum_nums += num
        # Выводим сумму, округленную до 9 знаков после запятой
        print(round(sum_nums, 9))
    except Exception as e:
        # Выводим сообщение об ошибке, если что-то пошло не так
        print(f"Alert: {e}")
