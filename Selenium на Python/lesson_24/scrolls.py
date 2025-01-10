

class Scrolls:
    """
    Класс Scrolls предоставляет методы для выполнения различных операций прокрутки страницы с использованием Selenium WebDriver.
    """

    def __init__(self, driver, action):
        """
        Инициализирует объект Scrolls с экземпляром WebDriver и ActionChains.

        :param driver: Экземпляр Selenium WebDriver.
        :param action: Экземпляр Selenium ActionChains для выполнения сложных действий.
        """
        self.driver = driver
        self.action = action

    def scroll_by(self, x, y):
        """
        Прокручивает страницу на заданное количество пикселей по горизонтали и вертикали.

        :param x: Количество пикселей для прокрутки по горизонтали.
        :param y: Количество пикселей для прокрутки по вертикали.
        """
        self.driver.execute_script(f"window.scrollTo({x}, {y})")

    def scroll_to_bottom(self):
        """
        Прокручивает страницу до самого низа.
        """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_top(self):
        """
        Прокручивает страницу до самого верха.
        """
        self.driver.execute_script("window.scrollTo(0, 0)")

    def scroll_to_element(self, element):
        """
        Прокручивает страницу до указанного элемента.
        Сначала использует ActionChains для перемещения к элементу, затем выполняет дополнительный скроллинг на 700 пикселей вниз.

        :param element: Веб-элемент, до которого нужно прокрутить страницу.
        """
        # Использует ActionChains для перемещения к элементу.
        self.action.scroll_to_element(element).perform()

        # Выполняет дополнительный скроллинг на 700 пикселей вниз от текущего положения.
        self.driver.execute_script("""
        window.scrollTo({
            top: window.scrollY + 700,
        });
        """)
