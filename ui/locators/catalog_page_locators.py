from selenium.webdriver.common.by import By


class CatalogPageLocators:
    """
    Локаторы страницы листинга каталога.
    """

    LOADER_BAR = (By.XPATH, ".//div[contains(@id, 'loading-bar')]")
    SORT_UP_BUTTON = (By.XPATH, ".//*[@data-test-id='sort-price-up-btn']")
    SORT_DOWN_BUTTON = (By.XPATH, ".//*[@data-test-id='sort-price-down-btn']")
    ALPHABET_SORT_BUTTON = (By.XPATH, ".//*[@data-test-id='sort-alphabet-btn']")
    ACTIVE_SORT_BUTTON = (By.XPATH, ".//*[contains(@data-test-id, 'sort') and contains(@class, 'is-active')]")
    PRODUCT_PRICE = (By.XPATH, ".//*[@data-test-id='product-price']")
    PRODUCT_BUTTON = (By.XPATH, ".//button[contains(@class, 'btn--blue2')]")
    PRODUCT_TITLE = (By.XPATH, ".//*[@data-test-id='product-title']")
    PRODUCT_CARD = (By.XPATH, ".//*[@data-test-id='product-item']")
    PRODUCT_CARD_BY_BTN_NAME = (By.XPATH, ".//button[text()='{0}']/ancestor::*[@data-test-id='product-item']")
    PRODUCT_BUTTON_BY_NAME = (By.XPATH, ".//button[contains(@class, 'btn--blue2') and contains(text(), '{0}')]")
    PAGINATION_ITEM = (By.XPATH, "//*[@data-test-id='pagination-page-btn']")
    PRODUCT_TITLE_BY_NAME = (By.XPATH, ".//*[@data-test-id='product-title' and contains(text(), '{0}')]")
