from api.base_api import BaseApi


class Auth(BaseApi):

    def get_test(self):
        url = 'api/app/stock/list'
        return self._get(url=url)
