import pytest
from random import choice
from allure import title, epic, feature, severity, severity_level
from data.data import CATALOG_LIST


@epic("Frontend")
@feature("Каталог")
class TestCatalog:
    """
    Тесты по продуктовому каталогу.
    """

    @pytest.mark.regress
    @pytest.mark.smoke
    @title("Сортировка по цене")
    @severity(severity_level.NORMAL)
    @pytest.mark.parametrize("sort_method", ("up", "down"))
    def test_catalog_sort_price(self, main_page, catalog_page, sort_method):
        catalog_url = choice(CATALOG_LIST)

        main_page.open()
        main_page.close_confirmation_popup()

        main_page.open(catalog_url)
        catalog_page.click_on_price_sort_button(sort_method)
        catalog_page.should_be_correct_price_sort(sort_method)

    @pytest.mark.regress
    @pytest.mark.smoke
    @title("Сортировка по алфавиту")
    @severity(severity_level.NORMAL)
    def test_catalog_sort_alphabet(self, main_page, catalog_page):
        catalog_url = choice(CATALOG_LIST)

        main_page.open()
        main_page.close_confirmation_popup()

        main_page.open(catalog_url)
        catalog_page.click_on_alphabet_sort_button()
        catalog_page.should_be_correct_alphabet_sort()

    @pytest.mark.smoke
    @pytest.mark.regress
    @title("Цена. Отображение в каталоге")
    @severity(severity_level.NORMAL)
    def test_show_price_in_catalog(self, main_page, catalog_page):
        catalog_url = choice(CATALOG_LIST)

        main_page.open()
        main_page.close_confirmation_popup()

        main_page.open(catalog_url)
        catalog_page.should_be_price_buy_product()
        max_page = catalog_page.get_max_page()
        catalog_page.go_to_catalog_page(category_url=catalog_url, page=max_page)
        catalog_page.should_be_price_reservation_product()

    @pytest.mark.regress
    @pytest.mark.smoke
    @title("Цена. В каталоге и карточке товара указана одна и та же цена")
    @severity(severity_level.NORMAL)
    def test_product_price_catalog_the_same(self, main_page, catalog_page, product_page):
        catalog_url = choice(CATALOG_LIST)

        main_page.open()
        main_page.close_confirmation_popup()

        main_page.open(catalog_url)
        products = catalog_page.get_product_list(available="available")
        if len(products) == 0:
            AssertionError(f'На странице: "{catalog_url}" - отсутствуют доступные товары')

        product = choice(products)
        catalog_page.click_product_by_name(product_name=product['name'])
        product_page.title_should_contain_product_name(product['name'])
        product_page.should_be_correct_product_price(expected_price=product['main_price'], place="каталоге")
