from json import load
from os.path import join
from pathlib import Path


def get_settings(environment):
    _root_dir = Path(__file__).parent.parent
    _config_path = join(_root_dir, 'config/config.json')
    with open(_config_path) as data:
        config = load(data)
        return config[environment]


def get_browser_config(browser_name):
    _root_dir = Path(__file__).parent.parent
    _config_path = join(_root_dir, 'config/browsers.json')
    with open(_config_path) as data:
        config = load(data)
        return config[browser_name]
