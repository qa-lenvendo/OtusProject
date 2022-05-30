from ui.pages.base_page import BasePage
from utils.ui_steps import step
from ui.locators.product_page_locators import ProductPageLocators as Locators


class ProductPage(BasePage):

    @step("Проверить соответствие цены товара с ценой в {place}")
    def should_be_correct_product_price(self, expected_price, place):
        """
        Сравнение цены товара с переданным значением.
        :param expected_price: значение цены, которое должно быть указано у товара.
        :param place: переменная для использования в отчетах. С какой ценой сравниваем (каталоге, базе данных).
        """
        product_price = self.string_to_num(self.find_element(*Locators.PRICE).text)

        assert product_price == float(expected_price), \
            f"Цена товара ({product_price}) не соответствует цене указанной в {place} ({expected_price})"

    @step("Проверка открытия страницы карточки товара")
    def title_should_contain_product_name(self, product_name):
        strategy, locator = Locators.PRODUCT_PAGE_TITLE
        assert self.is_element_present(strategy, locator.format(product_name)), \
            'Страница не открылась или заголовок не верный'
