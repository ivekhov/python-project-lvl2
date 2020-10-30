"""JSON files comparing correctness test."""

from gendiff.scripts.gendiff import generate_diff


def test_output():
	"""Check output."""
	output = generate_diff('file01.json', 'file02.json')
	expected = """{
  + verbose: True
  - follow: False
  - proxy: 123.234.53.22
    host: hexlet.io
  - timeout: 50
  + timeout: 20
}"""
	print(output)
	print(expected)
	assert output == expected


if __name__ == '__main__':
	test_output()