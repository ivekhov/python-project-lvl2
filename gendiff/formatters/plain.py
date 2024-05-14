from typing import Dict, List


def sort_tree(tree: List[Dict]) -> List[Dict]:
    """Sorting dicts inside list by value of 'node' value.

    Args:
        tree (List[Dict]): List of dicts with description of nodes.

    Returns:
        List[Dict]: Sorted list of dicts by 'node' value.
    """
    return sorted(tree, key=lambda item: item.get('node'))


def plain_strigify(current_value: object) -> str:
    """Convert object type to fix name in 'plain' string format.

    Args:
        current_value (object): Object for type identification.

    Returns:
        str: Name of object in string format.
    """
    if type(current_value) is dict:
        return '[complex value]'
    if current_value is None:
        return 'null'
    if current_value is True:
        return 'true'
    if current_value is False:
        return 'false'
    if type(current_value) is int:
        return f"{current_value}"
    return f"'{current_value}'"


def plain(diff_tree: List[Dict]) -> str:
    """Formatter of diff tree to 'plain' view.

    Args:
        tree (List): Difference between two files in tree format.

    Returns:
        str: String with result of comparison in 'plain' format.
    """
    def crawler(items, keys):
        sorted_items = sort_tree(items)

        def inner(current_item):
            match current_item.get('status'):
                case 'added':
                    nodes = '.'.join([*keys, current_item.get('node')])
                    plain = plain_strigify(current_item.get('value'))
                    return f"Property '{nodes}' was added with value: {plain}"
                case 'deleted':
                    nodes = '.'.join([*keys, current_item.get('node')])
                    return f"Property '{nodes}' was removed"
                case 'updated':
                    nodes = '.'.join([*keys, current_item.get('node')])
                    plain_old = plain_strigify(current_item.get('value_old'))
                    plain_new = plain_strigify(current_item.get('value_new'))
                    return (f"Property '{nodes}' was updated. "
                            f"From {plain_old} to {plain_new}")
                case 'nested':
                    return crawler(current_item.get('value'),
                                   [*keys, current_item.get('node')])
                case 'unchanged':
                    return
                case _:
                    raise ValueError("Unexpected status "
                                     f"{current_item.get('status')}")

        lines = list(map(inner, sorted_items))

        return '\n'.join(filter(lambda item: type(item) is str, lines))

    return crawler(diff_tree, [])
