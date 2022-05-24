#!/usr/bin/env python3

"""Script for gendiff usage."""

from gendiff.tools import generate_diff


def main():
    """Call main function of script."""
    diff = generate_diff(formatter='stylish')
    print(diff)


if __name__ == '__main__':
    main()
