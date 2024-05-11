def sort_tree(tree: list) -> list:
    return sorted(tree, key=lambda item: item.get('node'))


def plain_strigify(current_value):
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


def plain(diff_tree):
    def crawler(items, keys):
        sorted_items = sort_tree(items)

        def inner(current_item):
            match current_item.get('status'):
                case 'added':
                    return f"Property '{'.'.join([*keys, current_item.get('node')])}' was added with value: {plain_strigify(current_item.get('value'))}"
                case 'deleted':
                    return f"Property '{'.'.join([*keys, current_item.get('node')])}' was removed"
                case 'updated':
                    return f"Property '{'.'.join([*keys, current_item.get('node')])}' was updated. From {plain_strigify(current_item.get('value_old'))} to {plain_strigify(current_item.get('value_new'))}"
                case 'nested':
                    return crawler(current_item.get('value'), [*keys, current_item.get('node')])
                case 'unchanged':
                    return
                case _:
                    raise ValueError(f"Unexpected status {current_item.get('status')}")

        lines = list(map(inner, sorted_items))

        return '\n'.join(filter(lambda item: type(item) is str , lines))

    return crawler(diff_tree, [])