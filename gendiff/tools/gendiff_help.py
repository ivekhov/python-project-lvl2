#!/usr/bin/env python3

"""Script for gendiff help."""

import argparse


def gendiff_help():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    return parser.parse_args()
