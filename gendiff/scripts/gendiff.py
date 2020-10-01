"""Script for gendiff demo"""

import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')


if __name__ == '__main__':
    main()
