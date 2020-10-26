"""Starting point for comparing JSON files"""

import argparse
import json


PLUS = '  + '
MINUS = '  - '
EMPTY = '    '


def get_files():
    parser = argparse.ArgumentParser()
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    return args.first_file, args.second_file


def create_check_result(prefix, key, value, response):
    response.append(prefix)
    response.append(key)
    response.append(': ')
    response.append(str(value).lower().strip())
    response.append('\n')


def generate_diff(file_path1, file_path2):
    first = json.load(open(file_path1))
    second = json.load(open(file_path2))
    response = ['{', '\n']
    for key in second:
        if key in first.keys():
            if first[key] == second[key]:
                create_check_result(EMPTY, key, second[key], response)
            else:
                create_check_result(MINUS, key, first[key], response)
                create_check_result(PLUS, key, second[key], response)   
        else:
            create_check_result(PLUS, key, second[key], response)
    for key in first:
        if key not in second:
            create_check_result(MINUS, key, first[key], response)


    response.append('}')
    output = ''.join(response)
    return output


def main():
    files = get_files()
    diff = generate_diff(files[0], files[1])
    print(diff)


if __name__ == '__main__':
    main()
