from utils.ui_steps import step
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from re import sub


class BasePage:
    def __init__(self, ui):
        self.browser = ui.driver
        self.base_url = ui.base_url

    base_timeout = 20

    @step('Открыть страницу с адресом: {url}')
    def open(self, url: str = ''):
        self.browser.get(f"{self.base_url}/{url}")

    def is_element_present(self, strategy, locator, timeout=base_timeout) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(
                expected_conditions.presence_of_element_located((strategy, locator)),
            )
        except TimeoutException:
            return False
        return True

    def find_element(self, strategy: str, locator: str, timeout: int = base_timeout):
        return WebDriverWait(self.browser, timeout).until(
            expected_conditions.presence_of_element_located((strategy, locator)),
            message=f"Не найден элемент с локатором: {(strategy, locator)}")

    def find_elements(self, strategy, locator, timeout=base_timeout):
        return WebDriverWait(self.browser, timeout).until(
            expected_conditions.presence_of_all_elements_located((strategy, locator)),
            message=f"Не найден элемент с локатором: {(strategy, locator)}",
        )

    def find_element_clickable(self, strategy, locator, timeout=base_timeout):
        return WebDriverWait(self.browser, timeout).until(
            expected_conditions.element_to_be_clickable((strategy, locator)),
            message=f"Элемент с локатором: {(strategy, locator)} не доступен более {timeout} секунд")

    def is_not_element_visible(self, strategy, locator, timeout=base_timeout) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until_not(
                expected_conditions.visibility_of_element_located((strategy, locator)))
        except TimeoutException:
            return False
        return True

    def find_elements_visible(self, strategy, locator, timeout=base_timeout):
        return WebDriverWait(self.browser, timeout).until(
            expected_conditions.visibility_of_all_elements_located((strategy, locator)),
            message=f"Элементы с локатором: {(strategy, locator)} не отображаются более {timeout} секунд")

    def wait_is_not_element_present(self, strategy, locator, timeout=base_timeout, message=""):
        """
        Ожидание исчезновения искомого элемента на странице
        """
        WebDriverWait(self.browser, timeout).until_not(
            expected_conditions.presence_of_element_located((strategy, locator)),
            f"Элемент {message} не пропал со страницы более {timeout} секунд")

    def scroll_down(self):
        """
        Прокручивает страницу вниз
        """
        self.browser.execute_script("window.scrollBy(0, document.body.scrollHeight);")

    def scroll_up(self):
        """
        Прокручивает страницу вверх
        """
        self.browser.execute_script("window.scrollTo(0, -document.body.scrollHeight);")

    @staticmethod
    def string_to_num(value: str) -> float:
        """
        Очистка строки от символов не относящихся к числовому значению.(убирает все кроме чисел и точки)
        :param value: Строка из которой необходимо извлечь только float
        :return: значение с типом float
        """
        return float(sub(r"[^\d.]", "", value))
