"""JSON files comparing correctness test."""

# import pytest

from gendiff.scripts.gendiff import generate_diff


def read_correct(filename):
	with open(filename, 'r') as f:
		answer = f.readlines()
	return ''.join(answer)


def test_json():
	"""Check output."""
	output = generate_diff('./tests/fixtures/file01.json', './tests/fixtures/file02.json')
	expected = read_correct('./tests/fixtures/test_01_correct.txt')
	assert output == expected


def test_yaml():
	"""Check output."""
	output = generate_diff('./tests/fixtures/file03.yml', './tests/fixtures/file04.yml')
	expected = read_correct('./tests/fixtures/test_01_correct.txt')
	assert output == expected


def test_nested_json():
	"""Check output."""
	output = generate_diff('./tests/fixtures/file05.json', './tests/fixtures/file06.json')
	expected = read_correct('./tests/fixtures/test_02_correct.txt')
	assert output == expected
