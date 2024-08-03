# Копирование картинок из сайта перебором через url
import requests
from fake_useragent import UserAgent


headers = {'User-Agent': UserAgent().random}
for i in range(1, 161):
    response = requests.get(url=f'https://parsinger.ru/img_download/img/ready/{i}.png', headers=headers)
    with open(f'image{i}.png', 'wb') as image:
        image.write(response.content)
