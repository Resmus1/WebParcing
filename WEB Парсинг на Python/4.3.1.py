# Извлекаем информацию из скаченной страницы
from bs4 import BeautifulSoup

file_path = r'C:\PyCharm\WebParcing\Requests\files\index.html'
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
soup = BeautifulSoup(content, 'lxml')
print(soup)
