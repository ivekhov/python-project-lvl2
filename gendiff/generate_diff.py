from gendiff.tools.comparators import compare_objects
from gendiff.formatters import format_diff
from gendiff.tools.parsers import parse_file
from gendiff.tools.parsers import read_file_content
from gendiff.tools.parsers import get_file_extension
from gendiff.tools.parsers import get_file_path


def generate_diff(file_old, file_new, formatter='stylish'):
    '''
    '''
    file_path_old = get_file_path(file_old)
    file_path_new = get_file_path(file_new)

    file_content_old = read_file_content(file_path_old)
    file_content_new = read_file_content(file_path_new)

    file_extension_old = get_file_extension(file_path_old)
    file_extension_new = get_file_extension(file_path_new)

    try:
        file_extension_old != file_extension_new
    except Exception:
        raise NameError('File extensions are not equal: '
                        f'{file_extension_old}, ${file_extension_new}.')

    object_old = parse_file(file_content_old, file_extension_old)
    object_new = parse_file(file_content_new, file_extension_new)

    diff = compare_objects(object_old, object_new)

    return format_diff(diff, formatter)
