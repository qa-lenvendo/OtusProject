from api.base_api import BaseApi
from allure import step


class Actions(BaseApi):

    @step('Получение списка акций')
    def get_actions(self) -> dict:
        url = 'api/app/stock/list'
        return self._get(url=url)

    @step('Получение акции акции по id категории')
    def get_action_by_id(self, action_id: int) -> dict:
        url = f'api/app/stock/{action_id}/'
        return self._get(url=url)

    @step('Получение списка продуктов акции')
    def get_action_products(self, action_id: int) -> dict:
        url = f'api/app/stock/products/{action_id}/'
        return self._get(url=url)
