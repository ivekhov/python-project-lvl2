def sort_tree(tree: dict) -> list:
    # if tree.get('status') == 'nested':
    #     return sort_tree(tree.get('value'))

    # temp
    # return [list(item) for item in list(tree.items())]
    
    return sorted(tree, key=lambda item: item.get('node'))


def stringify(current_value, replacer, depth):
    if (type(current_value) is not dict):
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
        res.append(f'{current_indent}{key}: {stringify(value, replacer, depth + 1)}')
    lines = '\n'.join(res)

    return '\n'.join(["{", lines, f"{bracket_indent}}}"])


def stylish(diff_tree):
    TAB = '    '

    def crawler(list_, depth):

        current_indent = TAB * depth
        bracket_indent = TAB * (depth - 1)
        sorted_list = sort_tree(list_)

        def inner(current_item):
            match current_item.get('status'):
                case 'added':
                    return f"{current_indent[0:-2]}+ {current_item.get('node')}: {stringify(current_item.get('value'), TAB, depth + 1)}"
                case 'deleted':
                    return f"{current_indent[0:-2]}- {current_item.get('node')}: {stringify(current_item.get('value'), TAB, depth + 1)}"
                case 'updated':
                    return f"{current_indent[0:-2]}- {current_item.get('node')}: {stringify(current_item.get('value_old'), TAB, depth + 1)}\n{current_indent[0:-2]}+ {current_item.get('node')}: {stringify(current_item.get('value_new'), TAB, depth + 1)}"
                case 'unchanged':
                    return f"{current_indent}{current_item.get('node')}: {stringify(current_item.get('value'), TAB, depth + 1)}"
                case 'nested':
                    return f"{current_indent}{current_item.get('node')}: {crawler(current_item.get('value'), depth + 1)}"
                case _:
                    raise ValueError(f"Unexpected status {current_item.get('status')}")

        lines = list(map(inner, sorted_list))
        
        return '\n'.join(['{', *lines, f'{bracket_indent}}}'])

    return crawler(diff_tree, 1)