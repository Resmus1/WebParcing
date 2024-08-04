# Собрать ячейки залитые зеленым и сложить их значения
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

headers = {'User-Agent': UserAgent().random}
response = requests.get(url='https://parsinger.ru/table/4/index.html', headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
all_num = soup.find_all('td', class_='green')
sum_num = 0
for num in all_num:
    sum_num += float(num.text)
print(sum_num)