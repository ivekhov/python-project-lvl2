from typing import Dict, List


def sort_tree(tree: List[Dict]) -> List[Dict]:
    """Sorting dicts inside list by value of 'node' value.

    Args:
        tree (List[Dict]): List of dicts with description of nodes.

    Returns:
        List[Dict]: Sorted list of dicts by 'node' value.
    """
    return sorted(tree, key=lambda item: item.get('node'))


def stringify(current_value: object, replacer: str, depth: int) -> str:
    """Create a string in 'stylish' format recursively for object.

    Args:
        current_value (object): Object for type identification.

    Returns:
        str: Name of object in string format.
    """
    if type(current_value) is not dict:
        if current_value is None:
            return 'null'
        if current_value is True:
            return 'true'
        if current_value is False:
            return 'false'
        return f'{current_value}'

    indent_size = depth
    current_indent = replacer * indent_size
    bracket_indent = replacer * (indent_size - 1)

    res = []
    for key, value in current_value.items():
        res.append(
            f'{current_indent}{key}: {stringify(value, replacer, depth + 1)}'
        )
    lines = '\n'.join(res)

    return '\n'.join(["{", lines, f"{bracket_indent}}}"])


def stylish(diff_tree: List[Dict]) -> str:
    """Formatter of diff tree to 'stylish' view.

    Args:
        tree (List): Difference between two files in tree format.

    Returns:
        str: Result of comparison in 'stylish' format.
    """
    TAB = ' ' * 4

    def crawler(items, depth):

        current_indent = TAB * depth
        bracket_indent = TAB * (depth - 1)
        sorted_items = sort_tree(items)

        def inner(current_item):
            match current_item.get('status'):
                case 'added':
                    row = stringify(current_item.get('value'), TAB, depth + 1)
                    return (
                        f"{current_indent[0:-2]}+ "
                        f"{current_item.get('node')}: "
                        f"{row}"
                    )
                case 'deleted':
                    row = stringify(current_item.get('value'), TAB, depth + 1)
                    return (
                        f"{current_indent[0:-2]}- "
                        f"{current_item.get('node')}: {row}"
                    )
                case 'updated':
                    row_old = stringify(
                        current_item.get('value_old'), TAB, depth + 1
                    )
                    row_new = stringify(
                        current_item.get('value_new'), TAB, depth + 1
                    )
                    return (
                        f"{current_indent[0:-2]}- {current_item.get('node')}: "
                        f"{row_old}\n{current_indent[0:-2]}+ "
                        f"{current_item.get('node')}: {row_new}"
                    )
                case 'unchanged':
                    row = stringify(current_item.get('value'), TAB, depth + 1)
                    return (
                        f"{current_indent}{current_item.get('node')}: "
                        f"{row}"
                    )
                case 'nested':
                    return (
                        f"{current_indent}{current_item.get('node')}: "
                        f"{crawler(current_item.get('value'), depth + 1)}"
                    )
                case _:
                    raise ValueError("Unexpected status "
                                     f"{current_item.get('status')}")

        lines = list(map(inner, sorted_items))

        return '\n'.join(['{', *lines, f'{bracket_indent}}}'])

    return crawler(diff_tree, 1)
