import requests
from bs4 import BeautifulSoup

'''
Парсит картинки с сайта wishpics спсиком в указаной категории
'''

list_pics = []
link = "https://wishpics.ru/du-prikolnye/"
response = BeautifulSoup(requests.get(link).text, 'lxml')
div_pics = response.findAll('div', class_='img-wrapper')
for div in div_pics:
    img_tag = div.find('img')
    data_src = img_tag['data-src']
    list_pics.append(data_src)
print(list_pics)
