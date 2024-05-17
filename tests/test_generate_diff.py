import os
import pytest
from gendiff import generate_diff
from gendiff.tools.parsers import read_file_content


def get_fixture_path(file_name: str) -> str:
    """Creates full path to fixture file according to OS.

    Args:
        file_path (str): Fixture name.

    Returns:
        str: Full absolute path to fixture file.
    """
    return os.path.join(os.getcwd(), 'tests', 'fixtures', file_name)


@pytest.mark.parametrize(
    'file_before, file_after, formatter, expected',
    [
        [
            'file_before.json',
            'file_after.json',
            'stylish',
            'result_stylish.txt',
        ],
        [
            'file_before.json',
            'file_after.json',
            'plain',
            'result_plain.txt',
        ],
        [
            'file_before.yml',
            'file_after.yml',
            'stylish',
            'result_stylish.txt',
        ],
        [
            'file_before.yml',
            'file_after.yml',
            'plain',
            'result_plain.txt',
        ],
        [
            'file_extended_before.json',
            'file_extended_after.json',
            'stylish',
            'result_extended_stylish.txt',
        ],
        [
            'file_extended_before.json',
            'file_extended_after.json',
            'plain',
            'result_extended_plain.txt',
        ],
        [
            'file_extended_before.yml',
            'file_extended_after.yml',
            'stylish',
            'result_extended_stylish.txt',
        ],
        [
            'file_extended_before.yml',
            'file_extended_after.yml',
            'plain',
            'result_extended_plain.txt',
        ],
    ]
)
def test_gendiff(file_before, file_after, formatter, expected):
    path_before = get_fixture_path(file_before)
    path_after = get_fixture_path(file_after)
    path_expected = get_fixture_path(expected)

    assert generate_diff(path_before, path_after, formatter) == \
        read_file_content(path_expected)
