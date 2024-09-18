# Собрать данные с первого столбца и сложить их
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

headers = {'User-agent': UserAgent().random}
response = requests.get(url='https://parsinger.ru/table/2/index.html', headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
table = soup.find_all('tr')
sum_num = 0
for row in table[1:]:
    sum_num += float(row.text[1:6])
print(sum_num)