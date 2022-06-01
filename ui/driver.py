from pytest import UsageError
from selenium.webdriver import ChromeOptions, Remote, Chrome, FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from utils.helpers import get_settings


class UserInterface:
    def __init__(self, pytest_option):
        self.browser_name = pytest_option.getoption('--browser_name')
        self.headless = pytest_option.getoption('--headless')
        self.mode = pytest_option.getoption('--mode')
        self.hub = pytest_option.getoption('--hub')
        self.port = pytest_option.getoption('--hub_port')
        self.base_url = get_settings(pytest_option.getoption('--stand'))['SOURCE']
        self._window_width = 1920
        self._window_height = 1080

        options = self.get_options(browser_name=self.browser_name, headless=self.headless)
        options.add_argument("--disable-infobars")
        options.add_experimental_option("excludeSwitches", ["enable-automation", "ignore-certificate-errors"])

        if self.mode == "remote":
            if self.browser_name == 'chrome':
                options = ChromeOptions()
            elif self.browser_name == 'firefox':
                options = FirefoxOptions()
            else:
                raise AssertionError(f'Unknown browser: {self.browser_name}')

            self.driver = Remote(
                command_executor='http://' + self.hub + ':' + self.port + '/wd/hub',
                desired_capabilities=options.to_capabilities(),
                options=options
            )
        elif self.mode == "local":
            self.driver = Chrome(
                executable_path=ChromeDriverManager().install(),
                options=options,
                desired_capabilities=options.to_capabilities(),
            )
        else:
            raise UsageError("Unknown mode: {0}".format(pytest_option.getoption('--mode')))

        self.driver.set_window_size(1920, 1080)

    @staticmethod
    def get_options(browser_name, headless):
        if browser_name == "chrome":
            options = ChromeOptions()
            if headless == "true":
                options.add_argument("--headless")
            return options
        elif browser_name == "yandex":
            options = ChromeOptions()
            if headless == "true":
                options.add_argument("--headless")
            return options
        else:
            raise UsageError("Unknown browser: {0}".format(browser_name))

    def destroy(self):
        self.driver.quit()
