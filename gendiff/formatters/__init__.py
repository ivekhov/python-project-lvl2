from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from gendiff.formatters.jsonish import jsonish


def format_diff(diff, formatter):
    match formatter:
        case 'json':
            return jsonish(diff)
        case 'plain':
            return plain(diff)
        case 'stylish':
            return stylish(diff)
        case _:
            raise ValueError(f'Unknown formatter name {formatter}.')
