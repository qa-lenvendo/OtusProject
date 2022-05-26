from json import load
from os.path import join
from pathlib import Path
from glob import glob
from platform import system


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


def get_fixtures():
    fixtures = join(Path(__file__).parent.parent, 'fixtures')
    file_path = []
    for file in glob(f'{fixtures}/*'):
        file = file.split('/') if system().lower() in ['linux', 'darwin'] else file.split('\\')
        file = file[-1].split('.')[0]
        if file not in ['__init__', '__pycache__']:
            file_path.append(f'fixtures.{file}')
    return file_path
