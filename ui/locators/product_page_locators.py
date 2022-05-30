from selenium.webdriver.common.by import By


class ProductPageLocators:
    """
    Локаторы для страниц карточки товара.
    """
    PRODUCT_PAGE_TITLE = (By.XPATH, ".//*[@data-test-id='page-title' and contains(text(), '{0}')]")
    PRICE = (By.XPATH, ".//*[@class='b-price']//*[@data-test-id='product-price']")
