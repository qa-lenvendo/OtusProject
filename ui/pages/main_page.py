from ui.pages.base_page import BasePage
from utils.ui_steps import step
from ui.locators.main_page_locators import MainPageLocators as Locators


class MainPage(BasePage):

    def close_confirmation_popup(self):
        """
        Безусловное закрытие попапа подтверждения местоположения
        """
        if self.is_element_present(*Locators.LOCATION_CONFIRMATION_POPUP):
            self.click_button_on_confirmation_popup('yes')

    @step('Проверить наличие попапа подтверждения местоположения')
    def should_be_location_confirmation_popup(self):
        assert self.is_element_present(*Locators.LOCATION_CONFIRMATION_POPUP), \
            'Попап подтверждения местоположения отсутствует на странице'

    @step("Кликнуть по кнопке '{param}' в попапе подтверждения местоположения")
    def click_button_on_confirmation_popup(self, param: str = "yes"):
        """
        Нажатие на кнопки `Да/Нет` в попапе подтверждения местоположения.
        :param param: Передавать `yes` для нажатия на кнопку `Да` и `no` для нажатия на кнопку `Нет`
        """
        strategy, locator = Locators.BUTTON_CONFIRMATION_POPUP
        button = self.find_element(strategy, locator.format('Да' if param == 'yes' else 'Нет'))
        button.click()

    @step("Проверить корректность региона пользователя в шапке сайта")
    def should_be_user_region(self, region_name: str):
        """
        Проверка валидности региона пользователя в шапке сайта переданному значению.
        :param region_name: Наименование региона, который должен быть указан в шапке сайта пользователя
        """
        region_lnk = self.find_element(*Locators.HEADER_REGION_LNK)
        assert region_lnk.text == region_name, \
            f"Регион пользователя в шапке сайта ({region_lnk.text}) не соответствует ожидаемому ({region_name})"

    @step("Кликнуть по наименованию региона в шапке сайта")
    def click_region_lnk(self):
        """
        Клик по ссылке с наименованием региона пользователя в шапке сайта
        """
        region_lnk = self.find_element_clickable(*Locators.HEADER_REGION_LNK)
        region_lnk.click()
