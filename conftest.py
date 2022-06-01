from pytest import fixture
from ui.driver import UserInterface
from utils.helpers import get_fixtures

pytest_plugins = get_fixtures()


@fixture(scope='function')
def driver(request):
    driver = UserInterface(pytest_option=request.config)

    yield driver

    driver.destroy()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome')
    parser.addoption('--mode', action='store', default='local', help='Choose local or remote mode')
    parser.addoption('--stand', action='store', default='prod', help='Choose stand')
    parser.addoption("--hub", action="store", default=None, help="Choose hub host")
    parser.addoption("--hub_port", action="store", default=None, help="Choose hub port")
    parser.addoption("--headless", action="store", default="true", help="Choose headless mode: true or false")
