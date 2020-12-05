"""JSON files comparing correctness test."""

# import pytest

from gendiff.scripts.gendiff import generate_diff


def read_correct(filename):
	with open(filename, 'r') as f:
		answer = f.readlines()
	return ''.join(answer)


def test_output():
	"""Check output."""
	output = generate_diff('./tests/fixtures/file01.json', './tests/fixtures/file02.json')
	expected = read_correct('./tests/fixtures/test_01_correct.txt')
	assert output == expected
