from allure import title, epic, feature, severity, severity_level
from utils.helpers import validate_json_schema
import pytest
from data.data import STATIC_PAGE_SLUG
from random import randint


@epic('API')
@feature('Статические страницы')
class TestStaticPages:

    @title('Получение страницы по `slug`. Валидный запрос.')
    @severity(severity_level=severity_level.NORMAL)
    @pytest.mark.parametrize('slug_list', STATIC_PAGE_SLUG)
    def test_get_page_for_slug_200(self, api_static_page, slug_list):
        response = api_static_page.get_page_for_slug(slug_list)
        validate_json_schema(response=response, name='get_static_to_slug')

    @title('Получение страницы по `slug`. Невалидный запрос.')
    @severity(severity_level=severity_level.NORMAL)
    def test_get_page_for_slug_500(self, api_static_page):
        response = api_static_page.get_page_for_slug(f'{randint(100, 500)}')
        validate_json_schema(response=response, name='internal_error_500')

    @title('Получение маркетингового списка меню. Валидный запрос.')
    @severity(severity_level=severity_level.NORMAL)
    def test_get_top_menu_200(self, api_static_page):
        response = api_static_page.get_static_menu()
        validate_json_schema(response=response, name='get_static_menu')
