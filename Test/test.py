import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


headers = {'User-agent': UserAgent().random}
response = requests.get(url='https://parsinger.ru/html/headphones/5/5_32.html', headers=headers)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
div = soup.find('span', {'name': 'count'})
print(div)
