# Нужно посчитать через json стоимость товаров

import requests
from collections import defaultdict


def load_data(url):
    """Загружает данные из указанного URL и возвращает их в формате JSON."""
    response = requests.get(url=url)
    response.raise_for_status()  # Проверяет, был ли успешный запрос (статус 200)
    return response.json()


def cost_items_by_category(data):
    """
    Подсчитывает сумму товаров по категориям.
    Использует defaultdict(int), чтобы автоматически инициализировать значения как 0.
    """
    cost_lst = defaultdict(int)  # Создаем словарь с автоматическим значением по умолчанию 0
    for item in data:
        # Прибавляем значение 'cost' к соответствующей категории при этом срезая фразу ' руб'
        cost_lst[item['categories']] += int(item['price'][:-4])
    return cost_lst


def main():
    """Основная функция, которая загружает данные, подсчитывает количество и выводит результат."""
    url = 'https://parsinger.ru/downloads/get_json/res.json'
    data = load_data(url)  # Загружаем данные из URL
    cost_lst = cost_items_by_category(data)  # Подсчитываем цену товаров по категориям

    # Выводим на экран количество товаров для каждой категории
    for category, cnt_category in cost_lst.items():
        print(f"{category}: {cnt_category}")


if __name__ == "__main__":
    main()  # Запуск основной функции
