import requests
from fake_useragent import UserAgent

headers = {'User-agent': UserAgent().random, 'x-requested-with': 'XMLHttpRequest'}
response = requests.get(url='https://bitality.cc/', headers=headers)

# Проверка статуса ответа
if response.status_code == 200:
    try:
        data = response.json()
        print(data)
    except ValueError as e:
        print("Ошибка преобразования в JSON:", e)
        print("Содержимое ответа:", response.text)
else:
    print("Ошибка запроса:", response.status_code)