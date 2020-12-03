"""JSON files comparing correctness test."""

# import pytest

from gendiff.scripts.gendiff import generate_diff


def test_output():
	"""Check output."""
	output = generate_diff('./tests/fixtures/file01.json', './tests/fixtures/file02.json')
	expected = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""
	assert output == expected