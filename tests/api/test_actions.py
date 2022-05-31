from allure import title, epic, feature, severity, severity_level
from utils.helpers import validate_json_schema
from random import choice, randint


@epic('API')
@feature('Акции')
class TestActions:

    @title('Получение списка акций. Валидный запрос.')
    @severity(severity_level=severity_level.NORMAL)
    def test_get_actions_200(self, api_actions):
        response = api_actions.get_actions()
        validate_json_schema(response=response, name='get_actions')

    @title('Получения акции по id категории. Валидный запрос.')
    @severity(severity_level=severity_level.NORMAL)
    def test_get_action_by_id_200(self, api_actions):
        action = choice(choice(api_actions.get_actions()['list'])['list'])
        response = api_actions.get_action_by_id(action_id=action['id'])
        validate_json_schema(response=response, name='get_action_by_id')

    @title('Получения акции по id категории. Невалидный запрос.')
    @severity(severity_level=severity_level.NORMAL)
    def test_get_action_by_id_500(self, api_actions):
        action = randint(1000, 100000)
        response = api_actions.get_action_by_id(action_id=action)
        validate_json_schema(response=response, name='internal_error_500')

    @title('Получение товаров акции. Валидный запрос.')
    @severity(severity_level=severity_level.NORMAL)
    def test_get_products_action_200(self, api_actions):
        action = choice(choice(api_actions.get_actions()['list'])['list'])
        response = api_actions.get_action_products(action_id=action['id'])
        validate_json_schema(response=response, name='get_product_action')

    @title('Получение товаров акции. Невалидный запрос.')
    @severity(severity_level=severity_level.NORMAL)
    def test_get_products_action_500(self, api_actions):
        action = randint(1000, 100000)
        response = api_actions.get_action_products(action_id=action)
        validate_json_schema(response=response, name='internal_error_500')
