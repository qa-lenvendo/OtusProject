from ui.pages.main_page import MainPage
from pytest import fixture


@fixture(scope='function')
def main_page(driver):
    return MainPage(driver)
