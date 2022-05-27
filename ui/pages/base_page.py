from utils.ui_steps import step
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, ui):
        self.browser = ui.driver
        self.base_url = ui.base_url

    base_timeout = 10

    @step('Открыть страницу с адресом: {url}')
    def open(self, url: str = ''):
        self.browser.get(f"{self.base_url}/{url}")

    def find_element(self, strategy: str, locator: str, timeout: int = base_timeout):
        return WebDriverWait(self.browser, timeout).until(
            expected_conditions.presence_of_element_located((strategy, locator)),
            message=f"Не найден элемент с локатором: {(strategy, locator)}")
