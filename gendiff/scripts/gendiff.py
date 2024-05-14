import argparse
from gendiff import generate_diff


def main():
    """CLI utility for comparing difference of two files and format diff.

    Args:
        filepath1 (str): Path to first file.
        filepath2 (str): Path to second file.
        format (str): Optional, name of formatter.

    Returns:
        None: CLI print result in terminal.

    Example:
        $ gendiff file_before.json file_after.json
    """
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format',
                        default='stylish',
                        help='set format of output'
                        )
    parser.add_argument('filepath1')
    parser.add_argument('filepath2')

    diff = generate_diff(
        parser.parse_args().filepath1,
        parser.parse_args().filepath2,
        parser.parse_args().format
    )

    print(diff)


if __name__ == '__main__':
    main()
