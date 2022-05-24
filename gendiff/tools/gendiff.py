"""Help function for gendiff."""

import argparse
import json
import yaml


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


def parse_content(content):
    '''

    :param content:
    :return:
    '''


def formatter():
    pass


def generate_diff(file_path_01, file_path_02, formatter):
    file_01 = read_file(file_path_01)
    file_type_01 = get_file_type(file_path_01)
    content_01 = extract_content(file_01, file_type_01)


#

# parser = argparse.ArgumentParser(description='Generate diff')
# parser.add_argument('first_file')
# parser.add_argument('second_file')
# parser.add_argument('-f', '--format', help='set format of output')
# return parser.parse_args()


#ToDo
#1
# json.load(open()) = returns a dict
# yaml safe load return a dict



