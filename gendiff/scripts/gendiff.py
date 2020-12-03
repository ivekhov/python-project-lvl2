"""Starting point for comparing JSON files"""

import argparse
import json


PLUS = '  + '
MINUS = '  - '
EMPTY = '    '
OUTPUT_ROW_PATTERN = '{}{}: {}'


def get_files() -> (object, object):
    """
    Get files from command line arguments.

    Returns:
        file: first file for further comparing.
        file: second file for further comparing.

    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return args.first_file, args.second_file


def extend_buffer(prefix, key, value, output_buffer) -> list:
    """
    Append elements into list given. List is transformed by this function.

    Args:
        prefix: string constant.
        key: key from some dictionary.
        value: value of this key.
        output_buffer: array where these arguments are added.

    Returns:
        array: with added arguments.
    """
    output_buffer.append(OUTPUT_ROW_PATTERN.format(prefix, key, value))


def generate_diff(file_path1, file_path2) -> str:
    """
    Compare content of two files given and make output with result.

    Args:
        file_path1: first file path for comparing.
        file_path2: second file path for comparing.

    Returns:
        row with results of comparing.

    """
    with open(file_path1) as file_1:
        first = json.load(file_1)
    with open(file_path2) as file_2:
        second = json.load(file_2)
    new_keys = second.keys() - first.keys()
    deleted_keys = first.keys() - second.keys()
    common_keys = first.keys() & second.keys()
    all_keys = []
    for key in new_keys:
        all_keys.append(key)
    for key in deleted_keys:
        all_keys.append(key)
    for key in common_keys:
        all_keys.append(key)
    all_keys.sort()
    output_buffer = ['{']
    for key in all_keys:
        if key in new_keys:
            extend_buffer(PLUS, key, second[key], output_buffer)
        if key in deleted_keys:
            extend_buffer(MINUS, key, first[key], output_buffer)
        if key in common_keys:
            if first[key] == second[key]:
                extend_buffer(EMPTY, key, first[key], output_buffer)
            else:
                extend_buffer(MINUS, key, first[key], output_buffer)
                extend_buffer(PLUS, key, second[key], output_buffer)
    output_buffer.append('}')
    return '\n'.join(output_buffer)


def main():
    files = get_files()
    diff = generate_diff(files[0], files[1])
    print(diff)


if __name__ == '__main__':
    main()
