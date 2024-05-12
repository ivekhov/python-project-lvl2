import json
import os
import yaml


def get_file_extension(file_path):
    return file_path.split('.')[-1]


def get_file_path(file_name):
    return os.path.join(os.getcwd(), file_name)


def parse_file(file_content, file_extension):
    match file_extension.lower():
        case 'json':
            return json.loads(file_content)
        case 'yaml' | 'yml':
            return yaml.safe_load(file_content)
        case _:
            raise NameError(f'Format {file_extension} is incorrect.')


def read_file_content(file_path):
    with open(file_path) as file:
        return file.read()
