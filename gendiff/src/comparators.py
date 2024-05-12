def compare_objects(object_old, object_new):
    keys = set(object_old.keys()).union(object_new.keys())

    def inner(key):
        if key not in object_old.keys():
            return {
                'node': key,
                'status': 'added',
                'value': object_new[key]
            }
        if key not in object_new.keys():
            return {
                'node': key,
                'status': 'deleted',
                'value': object_old[key]
            }
        if type(object_new[key]) is dict and type(object_old[key]) is dict:
            return {
                'node': key,
                'status': 'nested',
                'value': compare_objects(object_old[key], object_new[key])
            }
        if object_new[key] == object_old[key]:
            return {
                'node': key,
                'status': 'unchanged',
                'value': object_old[key]
            }
        if object_new[key] != object_old[key]:
            if key in object_new.keys():
                return {
                    'node': key,
                    'status': 'updated',
                    'value_old': object_old[key],
                    'value_new': object_new[key]
                }
        raise ValueError('Objects are not comparable. Check input. '
                         f'{object_old} \n {object_new}')

    return list(map(inner, keys))
