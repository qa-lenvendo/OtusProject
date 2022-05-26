from pytest import fixture
from fixtures.ui import UserInterface


@fixture(scope='function')
def ui(request):
    ui = UserInterface(pytest_option=request.config)

    yield ui

    ui.destroy()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome')
    parser.addoption('--mode', action='store', default='local', help='Choose local or remote mode')
    parser.addoption('--stand', action='store', default='prod', help='Choose stand')
    parser.addoption("--hub", action="store", default=None, help="Choose hub host")
    parser.addoption("--hub_port", action="store", default=None, help="Choose hub port")
    parser.addoption("--headless", action="store", default="false", help="Choose headless mode: true or false")
