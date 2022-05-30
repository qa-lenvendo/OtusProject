from selenium.webdriver.common.by import By


class RegionPageLocators:
    """
    Локаторы попапа смены населенного пункта
    """

    LOADER = (By.XPATH, ".//div[contains(@class, 'el-loading-parent')]")
    REGION_POPUP = (By.XPATH, ".//*[@data-test-id='region-popup']")
    SEARCH_FIELD = (By.XPATH, ".//form/input[@data-test-id='input-search']")
    REGION_NAME = (By.XPATH, ".//*[@data-test-id='region-name']")
    SELECTED_REGION = (By.XPATH, ".//*[@data-test-id='selected-region']")
    CONFIRMATION_REGION_POPUP = (By.XPATH, ".//*[@data-test-id='confirmation-region-popup']")
    CONFIRMATION_REGION_POPUP_OK_BTN = (By.XPATH, ".//*[@data-test-id='ok-btn']")
