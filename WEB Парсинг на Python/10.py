# Собрать все данные с таблицы выделенным жирным и суммировать их
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

headers = {'User-Agent': UserAgent().random}
response = requests.get(url='https://parsinger.ru/table/3/index.html', headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
all_num = soup.find_all('td')
sum_b_num = 0
for b in all_num:
    b_num = b.find('b')
    if b_num:
        sum_b_num += float(b_num.text)
print(sum_b_num)
