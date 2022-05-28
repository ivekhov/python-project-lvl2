"""Help function for gendiff."""

import argparse
import json
import yaml

SPACE = ' '
MINUS = '-'
PLUS = '+'


def get_file_type(file_path) -> str:
    '''

    :param file_path, str type
    :return: file type ('json', 'yml', 'yaml',  etc)
    '''
    with open(file_path) as file:
        return file_path.split('.')[-1]


def read_file(file_path):
    '''

    :param file_path, str type
    :return: file
    '''
    with open(file_path) as file:
        return file


def extract_content(file, file_type):
    '''

    Read file, extract dict object and parse its content.

    :param: file (file), file_type (str)
    :return: dict
    '''
    if file_type == 'json':
        content = json.load(file)
    elif file_type == 'yaml' or file_type == 'yml':
        content = jaml.safe_load(file)

    return content


def get_difference(first, second) -> dict:

    intersection = set(first.keys()).intersection(set(second.keys()))
    first_only = set(first.keys()).difference(set(second.keys()))
    second_only = set(second.keys()).difference(set(first.keys()))

    for node in intersection:
        if type(first.get(node)) is dict:
            new_node = ' '.join([SPACE, str(node)])
            diff[new_node] = None
            get_difference(first.get(node), second.get(node))

        if first.get(node) == second.get(node):
            new_node = ' '.join([SPACE, str(node)])
            diff[new_node] = first.get(node)
        elif first.get(node) != second.get(node):
            diff[' '.join([MINUS, str(node)])] = second.get(node)
            diff[' '.join([PLUS, str(node)])] = first.get(node)

    for node in first_only:
        diff[' '.join([PLUS, str(node)])] = first.get(node)

    for node in second_only:
        diff[' '.join([MINUS, str(node)])] = second.get(node)


def generate_diff(file_path_01, file_path_02) -> dict:
    '''
    Generate diff between to dicts.

    :param file_path_01:
    :param file_path_02:
    :param formatter:
    :return:
    '''

    file_01 = read_file(file_path_01)
    file_type_01 = get_file_type(file_path_01)
    content_01 = extract_content(file_01, file_type_01)

    file_02 = read_file(file_path_02)
    file_type_02 = get_file_type(file_path_02)
    content_02 = extract_content(file_02, file_type_02)

    # ToDo
    diff = dict()
    get_difference(content_01, content_02)
    return diff


def stylish(diff) -> str:
    '''
    Formatting row for pretty printing.
    :param diff:
    :return: str
    '''
    result = ''

    # ToDo




    #
    return result


# parser = argparse.ArgumentParser(description='Generate diff')
# parser.add_argument('first_file')
# parser.add_argument('second_file')
# parser.add_argument('-f', '--format', help='set format of output')
# return parser.parse_args()



