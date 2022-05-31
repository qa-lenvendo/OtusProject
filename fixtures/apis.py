from pytest import fixture, hookimpl
from api.static_pages import StaticPages
from api.actions import Actions
from utils.helpers import get_settings

settings_config = {}


@hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    global settings_config
    settings_config = get_settings(environment=session.config.getoption("--stand"))


@fixture(scope='session')
def api_static_page():
    return StaticPages(settings_config['SOURCE'])


@fixture(scope='session')
def api_actions():
    return Actions(settings_config['SOURCE'])
