# Проходимся по таблице и делаем словарь, ключ это заголовок, а значение это сумма всех значений в столбце, округлить
# значения до 3‑х символов.
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

headers = {'User-Agent': UserAgent().random}
response = requests.get(url='https://parsinger.ru/table/5/index.html')
soup = BeautifulSoup(response.text, 'lxml')
rows = soup.find_all('tr')
list_rows = [row.text.split('\n') for row in rows]
list_rows = [[item for item in sublist if item] for sublist in list_rows]
colum = {list_rows[0][i]: 0.000 for i in range(len(list_rows[0]))}

for i in range(len(list_rows[0])):
    for j in range(1, len(list_rows)):
        colum[list_rows[0][i]] += float(list_rows[j][i])

for key in colum:
    colum[key] = round(colum[key], 3)

print(colum)
