import json
import os
from typing import Dict
import yaml


def get_file_extension(file_name: str) -> str:
    """Function for extracting file extension from file name.

    Args:
        file_name (str): File name.

    Returns:
        str: Type of file.
    """
    return file_name.split('.')[-1]


def get_file_path(file_name: str) -> str:
    """Generator of full path to file according to OS.

    Args:
        file_path (str): File name.

    Returns:
        str: Full absolute path to file.
    """
    return os.path.join(os.getcwd(), file_name)


def read_file_content(file_path: str) -> str:
    """Function for read file content from path into string.

    Args:
        file_path (str): Full absolute path to file.

    Returns:
        str: File content in string.
    """
    with open(file_path) as file:
        return file.read()


def parse_file(file_content: str, file_extension: str) -> Dict:
    """Parser of file content to Python dict() object.

    Args:
        file_content (str): File content in string format.
        file_extension (str): File extension.

    Returns:
        Dict: File content converted to dict() object.
    """
    match file_extension.lower():
        case 'json':
            return json.loads(file_content)
        case 'yaml' | 'yml':
            return yaml.safe_load(file_content)
        case _:
            raise NameError(f'Format {file_extension} is incorrect.')
