import pytest
from random import choice
from allure import title, epic, feature, severity, severity_level


@epic("Frontend")
@feature("Региональность")
class TestLocations:
    """
    Тесты для проверки региональности.
    """

    @pytest.mark.smoke
    @pytest.mark.regress
    @title('Первичный выбор региона')
    def test_primary_choice_of_region(self, main_page):
        region = "Город Москва"

        main_page.open()
        main_page.should_be_location_confirmation_popup()
        main_page.click_button_on_confirmation_popup("yes")
        main_page.should_be_user_region(region)

    @pytest.mark.regress
    @pytest.mark.smoke
    @title("Поиск региона")
    @severity(severity_level.NORMAL)
    @pytest.mark.parametrize("region_name", ("Брянская область", "Город Москва"))
    def test_search_region(self, main_page, region_page, region_name):
        main_page.open()
        main_page.close_confirmation_popup()

        main_page.click_region_lnk()
        region_page.can_see_region_popup()

        region_page.enter_text_into_search_field(region_name)
        region_page.can_see_region_on_search_result(region_name)

    @pytest.mark.regress
    @pytest.mark.smoke
    @title("Выбор другого региона через поисковую строку")
    @severity(severity_level.NORMAL)
    def test_select_other_region(self, main_page, region_page):
        region_name = "Город Санкт-Петербург"

        main_page.open()
        main_page.should_be_location_confirmation_popup()

        main_page.click_button_on_confirmation_popup("no")
        region_page.can_see_region_popup()

        region_page.enter_text_into_search_field(region_name)
        region_page.can_see_region_on_search_result(region_name)
        region_page.click_to_region_on_search_result(region_name)

        region_page.can_see_confirmation_region_popup()
        region_page.click_ok_in_confirmation_popup()

        main_page.should_be_user_region(region_name)

    @pytest.mark.regress
    @pytest.mark.smoke
    @title("Выбор другого региона из списка предложенных")
    @severity(severity_level.NORMAL)
    def test_select_other_region_in_list(self, main_page, region_page):

        main_page.open()
        main_page.should_be_location_confirmation_popup()

        main_page.click_button_on_confirmation_popup("no")
        region_page.can_see_region_popup()

        region_name = choice(region_page.get_region_list())

        region_page.click_on_region_from_the_list(region_name)
        region_page.can_see_region_on_search_result(region_name)

        region_page.click_to_selected_region()
        region_page.can_see_confirmation_region_popup()
        region_page.click_ok_in_confirmation_popup()

        main_page.should_be_user_region(region_name)
