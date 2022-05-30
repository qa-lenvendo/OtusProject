from ui.pages.base_page import BasePage
from utils.ui_steps import step
from ui.locators.region_popup_locators import RegionPageLocators as Locators
from allure import attach, attachment_type
from selenium.webdriver.common.keys import Keys


class RegionPage(BasePage):

    @step("Проверка наличия на странице попапа смены региона")
    def can_see_region_popup(self):
        """
        Проверка наличия попапа смены региона пользователя на странице
        """
        assert self.is_element_present(*Locators.REGION_POPUP), "На странице отсутствует попап смены региона"

    @step("Ввести значение в строку поиска региона")
    def enter_text_into_search_field(self, text):
        """
        Ввод текста в строку поиска региона.
        :param text: Текст который необходимо ввести в строку поиска
        """
        attach(str(text), "Вводимое значение", attachment_type=attachment_type.TEXT)

        search_field = self.find_element_clickable(*Locators.SEARCH_FIELD)

        search_field.click()
        search_field.clear()
        search_field.send_keys(text)
        search_field.send_keys(Keys.ENTER)

    @step("Проверка наличия искомого региона и схожих по наименованию регионов в поисковой выдаче")
    def can_see_region_on_search_result(self, region_name):
        """
        Проверка отображения среди поисковой выдачи искомого региона и схожих по семантике городов.
        :param region_name: Искомый регион или иной текст который должен присутствовать среди поисковой выдачи
        """
        if not self.is_not_element_visible(*Locators.LOADER):
            raise AssertionError(f"Загрузка элементов в попапе превысила {self.base_timeout} секунд")

        try:
            search_results = self.find_elements_visible(*Locators.REGION_NAME)
        except Exception:
            raise AssertionError("В попапе отсутствуют населенные пункты")

        names = [x.text.lower() for x in search_results]
        for name in names:
            assert (name.find(region_name.lower()) != -1), \
                f"Для искомого региона: `{region_name}` был найден невалидный регион с заголовком: `{name}`"

    @step("Кликнуть по кнопке `Хорошо` в попапе подтверждения смены региона")
    def click_ok_in_confirmation_popup(self):
        """
        Клик по кнопке `Хорошо` в попапе подтверждения смены региона
        """
        confirmation_btn = self.find_element_clickable(*Locators.CONFIRMATION_REGION_POPUP_OK_BTN)
        confirmation_btn.click()

    @step("Кликнуть по наименованию искомого региона в поисковой выдаче")
    def click_to_region_on_search_result(self, region_name):
        """
        Клик по наименованию региона в поисковой выдаче, если он соответствует переданному значению.
        :param region_name: Наименование региона
        """
        attach(str(region_name), "Наименование региона для клика", attachment_type=attachment_type.TEXT)

        self.find_element_clickable(*Locators.REGION_NAME)
        search_results = self.find_elements_visible(*Locators.REGION_NAME)

        for result in search_results:
            if result.text == region_name:
                result.click()
                break

    @step("Кликнуть по выбранному региону в попапе")
    def click_on_region_from_the_list(self, region_name):
        """
        Клик по региону с наименованием равным значению переданного параметра в списке регионов.
        :param region_name: Наименование региона по которому необходимо произвести клик
        """
        attach(str(region_name), "Наименование выбранного региона", attachment_type=attachment_type.TEXT)

        self.find_element_clickable(*Locators.REGION_NAME)
        region_list = self.find_elements(*Locators.REGION_NAME)
        for x in region_list:
            if x.text == region_name:
                x.click()
                break

    @step("Проверка отображения попапа подтверждения смены региона")
    def can_see_confirmation_region_popup(self):
        """
        Проверка отображения попапа подтверждения смены региона
        """
        assert self.is_element_present(*Locators.CONFIRMATION_REGION_POPUP), \
            "Попап подтверждения смены региона отсутствует на странице"

    @step('Кликнуть по названию региона в строке "Выбрать..."')
    def click_to_selected_region(self):
        """
        Клик по выбранному региону в строке `Выбрать`
        """
        selected_region = self.find_element_clickable(*Locators.SELECTED_REGION)
        selected_region.click()

    def get_region_list(self):
        """
        Получение списка наименований регионов в попапе смены населенного пункта.
        :return: Список наименований.
        """
        results = self.find_elements_visible(*Locators.REGION_NAME)
        return [x.text for x in results]
