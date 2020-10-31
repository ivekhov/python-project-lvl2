"""JSON files comparing correctness test."""

import pytest

from gendiff.scripts.gendiff import generate_diff


def test_output():
	"""Check output."""
	output = generate_diff('./tests/fixtures/file01.json', './tests/fixtures/file02.json')
	expected = """{
  + verbose: True
  - follow: False
  - proxy: 123.234.53.22
    host: hexlet.io
  - timeout: 50
  + timeout: 20
}"""
	assert output == expected


def test_():
	pass