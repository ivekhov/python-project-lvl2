import json


def jsonish(tree: list) -> list:
    return json.dumps(tree, indent=4)
