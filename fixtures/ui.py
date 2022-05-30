from ui.pages.main_page import MainPage
from ui.pages.region_page import RegionPage
from ui.pages.catalog_page import CatalogPage
from ui.pages.product_page import ProductPage
from pytest import fixture


@fixture(scope='function')
def main_page(driver):
    return MainPage(driver)


@fixture(scope='function')
def region_page(driver):
    return RegionPage(driver)


@fixture(scope='function')
def catalog_page(driver):
    return CatalogPage(driver)


@fixture(scope='function')
def product_page(driver):
    return ProductPage(driver)
