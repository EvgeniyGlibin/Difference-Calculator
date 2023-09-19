import itertools
from types import NoneType
import json


def format_the_value(value):
    if isinstance(value, NoneType | bool):
        value = json.dumps(value)
    elif isinstance(value, str):
        value = f"'{value}'"
    elif isinstance(value, dict):
        value = "[complex value]"
    return value


def get_plain_formater(value):

    def iter_(current_value, path):
        lines = []
        for dictionary in current_value:
            if dictionary['operation'] == 'nested':
                new_path = path + dictionary['key'] + "."
                lines.append(iter_(dictionary['new_value'], new_path))
            elif dictionary['operation'] == 'added':
                formatted_val = format_the_value(dictionary['new_value'])
                lines.append(f"Property '{path + dictionary['key']}'"
                             f" was added with value: {formatted_val}")
            elif dictionary['operation'] == 'removed':
                lines.append(f"Property '{path + dictionary['key']}'"
                             f" was removed")
            elif dictionary['operation'] == 'changed':
                formatted_val = format_the_value(dictionary['old_value'])
                formatted_val2 = format_the_value(dictionary['new_value'])
                lines.append(f"Property '{path + dictionary['key']}'"
                             f" was updated. From {formatted_val}"
                             f" to {formatted_val2}")
        result = itertools.chain(lines)
        return '\n'.join(result)

    return iter_(value, '')
