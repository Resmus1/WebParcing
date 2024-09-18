# Программа должна уметь следующее, вытаскивать со страницы нужную информацию и возможно анализировать

from selenium import webdriver
from selenium.webdriver.common.by import By

# Заранее подготовленный список десктопные User-Agent
desktop_user_agents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 "
    "Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 "
    "Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 "
    "Safari/537.36"
]


def initialize_browser():
    """Возвращаем откорректированную опцию веб драйвера"""
    pass

def enter_link():
    """Ввод ссылок для обработки и создание списка из них, а так же прекращает или продолжает программу"""

def parsing_info():
    """Вытаскивает нужные данные и создает словарь"""


def create_info():
    """Создает файл с информацией"""
    pass