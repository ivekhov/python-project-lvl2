import json


def jsonish(tree: list) -> list:
    # return f"{sorted(tree, key=lambda item: item.get('node'))}"
    return json.dumps(tree, indent=4)
