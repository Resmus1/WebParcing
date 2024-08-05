# Умножить число в оранжевой ячейке на число в синей и все сумировать
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

headers = {'User-agent': UserAgent().random}
response = requests.get(url='https://parsinger.ru/table/5/index.html', headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
all_row = soup.find_all('tr')
sum_num = 0
for row in all_row[1:]:
    sum_num += float(row.find('td', class_='orange').text) * float(row.find_all('td')[-1].text)
print(sum_num)
