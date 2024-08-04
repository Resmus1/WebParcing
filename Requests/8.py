# Собрать с таблицы данные и сложить их
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

headers = {'User-agent': UserAgent().random}
response = requests.get(url='https://parsinger.ru/table/1/index.html', headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
all_num = soup.find_all('td')
sum_num = 0
for num in all_num:
    sum_num += float(num.text)
print(sum_num)
