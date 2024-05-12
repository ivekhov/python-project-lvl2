def json(tree: list) -> list:
    return f"{sorted(tree, key=lambda item: item.get('node'))}"
