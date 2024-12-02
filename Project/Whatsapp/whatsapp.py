# Бот, который открывает ватсапп и делает рассылку гифки или заложеного месседжа.
# Нусжно создать список или генератор списка который на основании pics или других сайтов переберает адреса изображений и их отправляет, лучше просто использовать рандом нежели вести учет и добавить максимально возможное количество значений
# Добавить удаление изображения после использования

import os
import time
import logging
import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def clear_search_box(data_browser, position_search_box):
    """
    Очистка поля поиска перед отправкой следующего сообщения
    """
    try:
        actions = ActionChains(data_browser)
        actions.click(position_search_box).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(
            Keys.BACKSPACE).perform()
        logging.info("Поле поиска очищено")
    except Exception:
        logging.exception("Ошибка очистки поля поиска")


def download_image(url, save_path="downloaded_image.jpg"):
    """
    Скачивает изображение по URL и сохраняет его локально.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Проверка на ошибки HTTP
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        logging.info(f"Изображение скачано: {save_path}")
        return save_path
    except requests.exceptions.RequestException as e:
        logging.error(f"Ошибка загрузки изображения: {e}")
        return None


def save_as_jpg(file_path, output_path="processed_image.jpg"):
    """
    Пересохраняет изображение в формате JPG для устранения проблем с файлами.
    """
    try:
        img = Image.open(file_path)
        img = img.convert("RGB")  # Преобразование в RGB для совместимости
        img.save(output_path, "JPEG")
        logging.info(f"Изображение пересохранено как JPG: {output_path}")
        return os.path.abspath(output_path)
    except Exception as e:
        logging.error(f"Ошибка пересохранения изображения: {e}")
        return None


def wait_for_element(browser, by, locator, timeout=30):
    """
    Ожидание появления элемента на странице.
    """
    try:
        return WebDriverWait(browser, timeout).until(ec.presence_of_element_located((by, locator)))
    except Exception:
        logging.exception(f"Ошибка ожидания элемента: {locator}")
        return None


def send_image(data_browser, position_search_box, phone_number, image):
    """
    Отправка изображения по указанному номеру телефона через WhatsApp Web.
    """
    try:
        # Шаг 1: Очистка поля поиска
        clear_search_box(data_browser, position_search_box)

        # Шаг 2: Поиск контакта
        actions = ActionChains(data_browser)
        actions.click(position_search_box).send_keys(phone_number).send_keys(Keys.ENTER).perform()
        logging.info(f"Поиск контакта: {phone_number}")

        # Шаг 3: Ожидание загрузки чата
        wait_for_element(data_browser, By.XPATH, '//*[@id="main"]/footer')

        # Шаг 4: Нажатие кнопки прикрепления
        attach_button = wait_for_element(
            data_browser, By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[1]/div[2]'
        )
        if attach_button:
            attach_button.click()
            logging.info("Кнопка прикрепления нажата")

        # Шаг 5: Выбор файла
        file_input = wait_for_element(data_browser, By.XPATH, "(//input[@type='file'])[2]")
        if file_input:
            file_input.send_keys(image)
            logging.info(f"Изображение загружено: {image}")

        # Шаг 6: Пауза для завершения загрузки изображения
        time.sleep(2)

        # Шаг 7: Отправка сообщения
        # actions.send_keys(Keys.ENTER).perform()
        logging.info(f"Изображение отправлено контакту: {phone_number}")

    except Exception:
        logging.exception(f"Ошибка при отправке изображения контакту {phone_number}")


if __name__ == "__main__":
    try:
        # URL изображения
        image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSamK9SqgRR9pBMiq-K4qFOfiGBbKb33dQCpg&s"

        # Шаг 1: Скачивание изображения
        downloaded_path = download_image(image_url, "temp_image.jpg")

        # Шаг 2: Пересохранение изображения
        if downloaded_path:
            local_image_path = save_as_jpg(downloaded_path, "processed_image.jpg")

            # Шаг 3: Настройка браузера
            if local_image_path:
                options = webdriver.ChromeOptions()
                profile_path = r"C:\Users\ReSmus\AppData\Local\Google\Chrome\User Data"
                profile_name = "Default"
                options.add_argument(f"--user-data-dir={profile_path}")
                options.add_argument(f"--profile-directory={profile_name}")

                # Шаг 4: Открытие WhatsApp Web
                with webdriver.Chrome(options=options) as browser:
                    browser.get('https://web.whatsapp.com/')
                    time.sleep(10)  # Время для полной загрузки страницы

                    # Извлечение поля поиска
                    search_box = wait_for_element(browser, By.XPATH, '//*[@id="side"]/div[1]/div/div[2]')
                    if not search_box:
                        raise ValueError("Поле поиска не найдено")

                    # Список номеров и отправка изображения
                    phone_numbers = ['7014895907', '9005225039', '9333023533']
                    for number in phone_numbers:
                        send_image(browser, search_box, number, local_image_path)

    except FileNotFoundError as e:
        logging.error(f"Файл не найден: {e}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Ошибка запроса: {e}")
    except Exception as e:
        logging.exception("Непредвиденная ошибка:")
