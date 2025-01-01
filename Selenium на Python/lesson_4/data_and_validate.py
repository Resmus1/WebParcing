#  https://stepik.org/lesson/1140241/step/1?unit=1151914

from selenium import webdriver  # Импортируем webdriver для работы с браузером

try:
    # Открываем браузер Chrome
    with webdriver.Chrome() as browser:
        # Переходим на страницу GitHub репозитория
        browser.get('https://github.com/Resmus1/WebParcing')

        # Сохраняем текущий заголовок страницы
        current_title = browser.title

        # Переходим на сайт Google
        browser.get('https://www.google.com/')

        # Сохраняем текущий URL страницы (Google)
        current_url = browser.current_url

        # Переходим обратно на предыдущую страницу (GitHub)
        browser.back()

        # Проверяем, что после возвращения на предыдущую страницу, URL совпадает с сохранённым
        assert current_url == browser.current_url, "Error load url"  # Если URL не совпадает, выбрасывается ошибка

except Exception as e:
    # В случае ошибки выводим сообщение об ошибке
    print(e)
