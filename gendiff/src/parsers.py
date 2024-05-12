import json
import yaml


def parse_file(file_content, file_extension):
    match file_extension:
        case 'json':
            return json.loads(file_content)
        case 'yaml' | 'yml':
            return yaml.safe_load(file_content)
        case _:
            raise NameError(f'Format {file_extension} is incorrect.')
