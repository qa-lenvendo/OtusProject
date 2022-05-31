from json import load
from os.path import join
from pathlib import Path
from glob import glob
from platform import system
from allure import step
import mimesis.exceptions
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate


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


@step('Валидация ответа API по схеме: "{name}"')
def validate_json_schema(response, name):
    """
    A method for verifying the validation of a test result based on a json schema
    :param response: Response from the server
    :param name: JSON schema name
    """
    def validate_json(resp, schema_name):
        _root_dir = Path(__file__).parent.parent
        _json_schema_path = join(_root_dir, 'json_schema', schema_name + '.json')
        with open(_json_schema_path) as file:
            json_file = load(file)
        try:
            validate(instance=resp, schema=json_file)
            return True
        except mimesis.exceptions.SchemaError:
            print('JSON cхема содержит ошибку')
        except ValidationError as e:
            print('Ошибка: ', e)
        except Exception as e:
            print(e)
        return False

    assert validate_json(resp=response, schema_name=name), 'Ответ API не соответствует JSON схеме'
