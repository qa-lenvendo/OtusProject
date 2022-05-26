from requests import delete, get, patch, post


class BaseApi:
    def __init__(self, base_url):
        self.base_url = base_url

    def _get(self, url='/', headers=None, auth=None):
        """
        Method for sending a GET request to the server

        :param url: Request URL
        :param headers: Request headers
        :param auth: Basic authorization on the server
        :return: Response in JSON format
        """
        if headers is None:
            headers = {}
        if auth is None:
            auth = ()
        return get(url=f'{self.base_url}/{url}', verify=False, headers=headers, auth=auth)
