import os
import pytest
from gendiff.generate_diff import generate_diff


EXTENSIONS = [
    'json', 
    'yml',
]


def get_fixture_path(file_name):
    return os.path.join(os.getcwd(), '.', 'tests', 'fixtures', file_name)


def read_file_content(file_path):
    with open(file_path) as file:
        return file.read() 


@pytest.fixture
def correct_stylish():
    return read_file_content(get_fixture_path('result_stylish.txt'))


@pytest.fixture
def correct_plain():
    return read_file_content(get_fixture_path('result_plain.txt'))


def test_stylish(correct_stylish):
    for ext in EXTENSIONS:
        file_before = get_fixture_path(f'file_before.{ext}')
        file_after = get_fixture_path(f'file_after.{ext}')
        assert generate_diff(file_before, file_after, 'stylish') == correct_stylish


def test_plain(correct_plain):
    for ext in EXTENSIONS:
        file_before = get_fixture_path(f'file_before.{ext}')
        file_after = get_fixture_path(f'file_after.{ext}')
        assert generate_diff(file_before, file_after, 'plain') == correct_plain


@pytest.fixture
def correct_extended_stylish():
    return read_file_content(get_fixture_path('result_extended_stylish.txt'))


@pytest.fixture
def correct_extended_plain():
    return read_file_content(get_fixture_path('result_extended_plain.txt'))


def test_extended_stylish(correct_extended_stylish):
    for ext in EXTENSIONS:
        file_before = get_fixture_path(f'file_extended_before.{ext}')
        file_after = get_fixture_path(f'file_extended_after.{ext}')
        assert generate_diff(file_before, file_after, 'stylish') == correct_extended_stylish


def test_extended_plain(correct_extended_plain):
    for ext in EXTENSIONS:
        file_before = get_fixture_path(f'file_extended_before.{ext}')
        file_after = get_fixture_path(f'file_extended_after.{ext}')
        assert generate_diff(file_before, file_after, 'plain') == correct_extended_plain