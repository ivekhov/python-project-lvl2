import os
import pytest
from gendiff import generate_diff


def get_fixture_path(file_name):
    return os.path.join(os.getcwd(), 'tests', 'fixtures', file_name)


def read_file_content(file_path):
    with open(file_path) as file:
        return file.read()


@pytest.fixture
def file_before_json():
    return get_fixture_path('file_before.json')


@pytest.fixture
def file_after_json():
    return get_fixture_path('file_after.json')


@pytest.fixture
def file_before_yml():
    return get_fixture_path('file_before.yml')


@pytest.fixture
def file_after_yml():
    return get_fixture_path('file_after.yml')


@pytest.fixture
def correct_stylish():
    return read_file_content(get_fixture_path('result_stylish.txt'))


@pytest.fixture
def correct_plain():
    return read_file_content(get_fixture_path('result_plain.txt'))


@pytest.fixture
def correct_extended_stylish():
    return read_file_content(get_fixture_path('result_extended_stylish.txt'))


@pytest.fixture
def correct_extended_plain():
    return read_file_content(get_fixture_path('result_extended_plain.txt'))


@pytest.mark.parametrize(
    ["file_before", "file_after", "formatter", "expected"],
    [
        [
            'file_before_json',
            'file_after_json',
            'stylish',
            'correct_stylish',
        ],
        [
            'file_before_json',
            'file_after_json',
            'plain',
            'correct_plain',
        ],
        [
            'file_before_yml',
            'file_after_yml',
            'stylish',
            'correct_stylish',
        ],
        [
            'file_before_yml',
            'file_after_yml',
            'plain',
            'correct_plain',
        ],
    ]
)
def test_gendiff(file_before, file_after, formatter, expected, request):
    file_before = request.getfixturevalue(file_before)
    file_after = request.getfixturevalue(file_after)
    expected = request.getfixturevalue(expected)
    assert generate_diff(file_before, file_after, formatter) == expected


@pytest.fixture
def file_extended_before_json():
    return get_fixture_path('file_extended_before.json')


@pytest.fixture
def file_extended_after_json():
    return get_fixture_path('file_extended_after.json')


@pytest.fixture
def file_extended_before_yml():
    return get_fixture_path('file_extended_before.yml')


@pytest.fixture
def file_extended_after_yml():
    return get_fixture_path('file_extended_after.yml')


@pytest.mark.parametrize(
    ["file_before", "file_after", "formatter", "expected"],
    [
        [
            'file_extended_before_json',
            'file_extended_after_json',
            'stylish',
            'correct_extended_stylish',
        ],
        [
            'file_extended_before_json',
            'file_extended_after_json',
            'plain',
            'correct_extended_plain',
        ],
        [
            'file_extended_before_yml',
            'file_extended_after_yml',
            'stylish',
            'correct_extended_stylish',
        ],
        [
            'file_extended_before_yml',
            'file_extended_after_yml',
            'plain',
            'correct_extended_plain',
        ],
    ]
)
def test_gendiff_extended(file_before, file_after,
                          formatter, expected, request):
    file_before = request.getfixturevalue(file_before)
    file_after = request.getfixturevalue(file_after)
    expected = request.getfixturevalue(expected)
    assert generate_diff(file_before, file_after, formatter) == expected
