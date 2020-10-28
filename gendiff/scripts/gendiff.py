"""Starting point for comparing JSON files"""

import argparse
import json


PLUS = '  + '
MINUS = '  - '
EMPTY = '    '


def get_files() -> (object, object):
    """
    Get files from command line arguments.

    Returns:
        file: first file for further comparing.
        file: second file for further comparing.

    """
    parser = argparse.ArgumentParser()
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    return args.first_file, args.second_file


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
            output_buffer = ['{']
            new_keys = list(second.keys() - first.keys())
            deleted_keys = list(first.keys() - second.keys())
            common_keys = list(first.keys() & second.keys())
            for key in new_keys:
                output_buffer.append('{}{}: {}'.format(PLUS, key, str(second[key]).strip()))
            for key in deleted_keys:
                output_buffer.append('{}{}: {}'.format(MINUS, key, str(first[key]).strip()))
            for key in common_keys:
                if first[key] == second[key]:
                    output_buffer.append('{}{}: {}'.format(EMPTY, key, str(first[key]).strip()))
                else:
                    output_buffer.append('{}{}: {}'.format(MINUS, key, str(first[key]).strip()))                
                    output_buffer.append('{}{}: {}'.format(PLUS, key, str(second[key]).strip()))
    output_buffer.append('}')
    return '\n'.join(output_buffer)


def main():
    files = get_files()
    diff = generate_diff(files[0], files[1])
    print(diff)


if __name__ == '__main__':
    main()
