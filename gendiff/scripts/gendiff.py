import argparse
from gendiff.src.gendiff import generate_diff


def main():
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
