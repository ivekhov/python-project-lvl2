def json(tree: list) -> list:    
    return sorted(tree, key=lambda item: item.get('node'))