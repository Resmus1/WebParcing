# Найти сумму всех сумму на сайте
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

headers = {'User-agent': UserAgent().random}
response = requests.get(url='https://parsinger.ru/html/index1_page_1.html', headers=headers)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
costs = soup.find_all('p', class_='price')
sum_costs = 0
for cost in costs:
    sum_costs += int(''.join(i if i.isdigit() else '' for i in cost.text))
print(sum_costs)
