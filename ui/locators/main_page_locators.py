from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    Локаторы для главной страницы.
    """

    LOCATION_CONFIRMATION_POPUP = (By.XPATH, ".//article[contains(@class, 'b-header-info')]")
    BUTTON_CONFIRMATION_POPUP = (By.XPATH, ".//button[contains(text(), '{0}')]")
    HEADER_REGION_LNK = (By.XPATH, ".//*[@data-test-id='region-link']/span")
