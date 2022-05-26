from pytest import fixture, hookimpl
from api.auth import Auth
from utils.helpers import get_settings

settings_config = {}


@hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    global settings_config
    settings_config = get_settings(environment=session.config.getoption("--stand"))


@fixture(scope='session')
def api_auth():
    return Auth(settings_config['SOURCE'])
