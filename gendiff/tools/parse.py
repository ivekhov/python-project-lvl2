"""Tools for parsing files"""

import json
import yaml


def parse_files(file_path1, file_path2) -> list:
    """
    Compare content of two files given and make output with result.

    Args:
        file_path1: first file for comparing.
        file_path2: second file for comparing.

    Returns:
        list with dicts for further comparing.

    """
    with open(file_path1) as file_1:
        file_format = file_path1.split('.')[-1]
        if file_format == 'json':
            first = json.load(file_1)
        elif file_format == 'yml':
            first = yaml.safe_load(file_1)
    with open(file_path2) as file_2:
        file_format = file_path2.split('.')[-1]
        if file_format == 'json':
            second = json.load(file_2)
        elif file_format == 'yml':
            second = yaml.safe_load(file_2)
    return [first, second]
