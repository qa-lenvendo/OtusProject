from api.base_api import BaseApi
from allure import step


class StaticPages(BaseApi):

    @step('Получение страницы по slug')
    def get_page_for_slug(self, slug):
        url = f'api/app/{slug}'
        return self._get(url=url)

    @step('Получение пунктов статичных пунктов меню')
    def get_static_menu(self):
        url = 'api/app/pages/menu'
        return self._get(url=url)
