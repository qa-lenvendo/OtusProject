from ui.pages.base_page import BasePage
from utils.ui_steps import step
from ui.locators.catalog_page_locators import CatalogPageLocators as Locators
from allure import attach, attachment_type


class CatalogPage(BasePage):

    def wait_page_loaded(self):
        strategy, locator = Locators.LOADER_BAR
        if self.is_element_present(strategy, locator, 4):
            self.wait_is_not_element_present(strategy, locator, 15, "loader")

    @step("Кликнуть по кнопке сортировки цены")
    def click_on_price_sort_button(self, method: str = "up"):
        """
        Клик по кнопкам сортировки по убыванию/возрастанию цены.
        :param method: Метод сортировки. up - по возрастанию цены, down - по убыванию цены
        """
        _method = "По возрастанию" if method == "up" else "По убыванию"
        attach(str(_method), "Метод сортировки", attachment_type=attachment_type.TEXT)

        if method == "up":
            button = self.find_element_clickable(*Locators.SORT_UP_BUTTON)
        else:
            button = self.find_element_clickable(*Locators.SORT_DOWN_BUTTON)

        button.click()

        self.wait_page_loaded()

    @step("Проверить сортировки товаров по цене")
    def should_be_correct_price_sort(self, method: str):
        """
        Проверка корректности сортировки товаров "По цене" на странице каталога.
        :param method: метод сортировки по которому должны быть отсортированы товары на странице каталога
        """
        method_type = "по возрастанию цены" if method == "up" else "по убыванию цены"
        attach(method_type, "Метод сортировки", attachment_type.TEXT)

        product_list = self.get_product_list(available="all")
        null_price = [x for x in product_list if x['main_price'] == 0]
        not_null_price = [x for x in product_list if x['main_price'] > 0]

        if method == "up":
            expected_product_list = sorted(not_null_price, key=lambda i: i['main_price'])
        elif method == "down":
            expected_product_list = sorted(not_null_price, key=lambda i: i['main_price'], reverse=True)
        else:
            raise ValueError('Передано не верное значение в параметр "method"')

        expected_product_list.extend(null_price)

        for x in range(len(product_list)):
            assert (product_list[x]['main_price'] == expected_product_list[x]['main_price']), \
                f"Товар с заголовком `{product_list[x]['name']}` отсортирован не верно"

    def get_product_list(self, available: str = "all") -> list:
        """
        Получение списка товаров со страницы каталога.
        :param available: допустимые значения: ['available', 'not_available', 'reservation', 'all']
        :return: в зависимости от переданного значения возвращает списки товаров 'Доступных для покупки'
        или 'Недоступных для покупки' или 'Доступных для бронирования' или 'Всех' товаров
        """
        if available not in ['available', 'not_available', 'reservation', 'all']:
            ValueError('Не верное значение для параметра "available"')

        self.scroll_down()
        product_list = []

        try:
            if available == "available":
                btn_name = "В корзину"
                strategy, locator = Locators.PRODUCT_CARD_BY_BTN_NAME
                products = self.find_elements(strategy, locator.format(btn_name))

                for product in products:
                    name = product.find_element(*Locators.PRODUCT_TITLE).text
                    btn_strategy, btn_locator = Locators.PRODUCT_BUTTON_BY_NAME
                    buy_btn = product.find_element(btn_strategy, btn_locator.format(btn_name))
                    try:
                        price = self.string_to_num(product.find_element(*Locators.PRODUCT_PRICE).text)
                    except Exception:
                        price = 0

                    product_list += [dict(name=name, main_price=price, buy_btn=buy_btn)]

            elif available == "reservation":
                btn_name = "Забронировать"
                strategy, locator = Locators.PRODUCT_CARD_BY_BTN_NAME
                products = self.find_elements(strategy, locator.format(btn_name))

                for product in products:
                    name = product.find_element(*Locators.PRODUCT_TITLE).text
                    btn_strategy, btn_locator = Locators.PRODUCT_BUTTON_BY_NAME
                    buy_btn = product.find_element(
                        btn_strategy, btn_locator.format(btn_name),
                    )
                    try:
                        price = float(
                            self.string_to_num(
                                product.find_element(*Locators.PRODUCT_PRICE).text,
                            ),
                        )
                    except Exception:
                        price = 0
                    product_list.append(dict(name=name, main_price=price, buy_btn=buy_btn))

            elif available == "not_available":
                strategy, locator = Locators.PRODUCT_CARD_BY_BTN_NAME
                products_absent = []
                products_not_available = []
                if self.is_element_present(strategy, locator.format("Нет в наличии"), 10):
                    products_not_available = self.find_elements(strategy, locator.format("Нет в наличии"))
                if self.is_element_present(strategy, locator.format("Временно отсутствует"), 10):
                    products_absent = self.find_elements(strategy, locator.format("Временно отсутствует"))
                products = products_absent + products_not_available

                for product in products:
                    name = product.find_element(*Locators.PRODUCT_TITLE).text
                    product_list.append(dict(name=name))

            elif available == "all":
                products_not_available = self.find_elements(*Locators.PRODUCT_CARD)

                for product in products_not_available:
                    name = product.find_element(*Locators.PRODUCT_TITLE).text
                    buy_btn = product.find_element(*Locators.PRODUCT_BUTTON)
                    try:
                        price = self.string_to_num(product.find_element(*Locators.PRODUCT_PRICE).text)
                    except Exception:
                        price = 0
                    product_list.append(dict(name=name, main_price=price, buy_btn=buy_btn))

        except Exception:
            product_list = []

        return product_list

    @step('Кликнуть по кнопке сортировки "По алфавиту"')
    def click_on_alphabet_sort_button(self):
        """
        Клик по кнопке сортировки "По алфавиту" (сортировка от А до Я)
        """
        button = self.find_element_clickable(*Locators.ALPHABET_SORT_BUTTON)
        button.click()

        self.wait_page_loaded()

    @step("Проверить активность сортировки 'По алфавиту'")
    def should_be_active_alphabet_sort(self):
        """
        Проверка активности сортировки по алфавиту.
        """
        sort_active = self.find_element(*Locators.ACTIVE_SORT_BUTTON).text
        assert sort_active.lower() == "по алфавиту", "Сортировка 'По алфавиту' не активна"

    @step("Проверка сортировки товаров `По алфавиту`")
    def should_be_correct_alphabet_sort(self):
        """
        Проверка корректности сортировки товаров "По алфавиту"
        """
        product_list = self.get_product_list(available="all")
        product_list = [x for x in product_list if x['buy_btn'] is not None]
        expected_product_list = sorted(product_list, key=lambda i: i['name'])

        for x in range(len(product_list)):
            assert (product_list[x]['name'] == expected_product_list[x]['name']), \
                f"Товар с заголовком `{product_list[x]['name']}` отсортирован не верно"

    @step("Проверка наличия цен у товаров доступных для покупки")
    def should_be_price_buy_product(self):
        """
        Проверка наличия цен у товаров доступных для покупки.
        """
        product_list = self.get_product_list(available="available")
        available_products = [x for x in product_list if x['buy_btn'] is not None]

        buy_products = []
        for x in available_products:
            if x['buy_btn'].text.lower() == "в корзину":
                buy_products.append(x)

        for x in buy_products:
            assert (x['main_price'] > 0), f"У товара с наименованием {x['name']} отсутствует цена"

    def get_max_page(self) -> int:
        """
        Получение количества страниц в листинге каталога.
        """
        pagination_list = self.find_elements(*Locators.PAGINATION_ITEM)
        return int(pagination_list[len(pagination_list) - 1].text)

    @step("Перейти на страницу категории: {category_url}, и номером: {page}")
    def go_to_catalog_page(self, category_url: str, page: int):
        """
        Переход на определенную страницу категории.
        :param category_url: относительный url категории.
        :param page: номер страницы, на которую нужно перейти.
        """
        connection_symbol = "?" if "?" not in category_url else "&"
        self.open(f"{category_url}{connection_symbol}page={page}")

    @step("Проверка наличия цен у товаров доступных для бронирования")
    def should_be_price_reservation_product(self):
        """
        Проверка наличия цен у товаров доступных для бронирования.
        """
        product_list = self.get_product_list(available="reservation")
        available_products = [x for x in product_list if x['buy_btn'] is not None]

        reservation_products = []
        for x in available_products:
            if x['buy_btn'].text.lower() == "забронировать":
                reservation_products.append(x)

        for x in reservation_products:
            assert (x['main_price'] > 0), f"У товара с наименованием {x['name']} отсутствует цена"

    @step("Кликнуть по ссылке товара с наименованием: {product_name}")
    def click_product_by_name(self, product_name: str):
        """
        Клик по ссылке с наименованием товара, для перехода в карточку товара.
        :param product_name: Наименование товара по которому необходимо кликнуть.
        """
        strategy, locator = Locators.PRODUCT_TITLE_BY_NAME
        link = self.find_element_clickable(strategy, locator.format(product_name))
        link.click()
