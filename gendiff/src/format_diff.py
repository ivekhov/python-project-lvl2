from .formatters.plain import plain
from .formatters.stylish import stylish
from .formatters.json import json as jsonish


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