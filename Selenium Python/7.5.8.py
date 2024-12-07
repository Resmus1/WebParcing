#  https://stepik.org/lesson/732079/step/8?unit=733612

from selenium import webdriver  # Импортируем WebDriver для взаимодействия с веб-браузером
from selenium.webdriver.chrome.options import Options  # Импортируем Options для настройки браузера
from selenium.webdriver.common.by import By  # Импортируем локаторы для поиска элементов на странице

# Список URL-адресов для взаимодействия
sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html',
         'http://parsinger.ru/blank/1/3.html', 'http://parsinger.ru/blank/1/4.html',
         'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html']

# Настройки для браузера Chrome
options = Options()
options.add_argument('--headless==new')  # Запускаем браузер в фоновом режиме (без графического интерфейса)

if __name__ == '__main__':
    sum_nums = 0  # Переменная для хранения суммы чисел
    try:
        browser = webdriver.Chrome()  # Инициализируем экземпляр браузера Chrome
        for site in sites:  # Проходим по каждому URL в списке
            browser.execute_script(f"window.open('{site}')")  # Открываем новый таб с текущим URL
            browser.get(site)  # Переходим на страницу по указанному URL
            browser.find_element(By.CLASS_NAME, 'checkbox_class').click()  # Кликаем на чекбокс с указанным классом
            num = int(browser.find_element(By.ID, 'result').text) ** 0.5  # Берем текст из элемента с ID "result" и вычисляем квадратный корень
            sum_nums += num  # Добавляем результат к общей сумме
        print(round(sum_nums, 9))  # Выводим сумму, округленную до 9 знаков после запятой
    except Exception as e:  # Обрабатываем исключения
        print(f"Alert: {e}")  # Выводим сообщение об ошибке, если что-то пошло не так
