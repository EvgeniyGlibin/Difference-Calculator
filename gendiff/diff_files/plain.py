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
        keys = current_value.keys()
        for key, val in current_value.items():
            key = str(key)
            formatted_val = format_the_value(val)
            if key.startswith('  ') and isinstance(
                    val, dict) is True:
                new_path = path + key[2:] + "."
                lines.append(iter_(val, new_path))
            elif key.startswith('+ ') and '- ' + key[2:] not in keys:
                lines.append(f"Property '{path + key[2:]}'"
                             f" was added with value: {formatted_val}")
            elif key.startswith('- ') and '+ ' + key[2:] not in keys:
                lines.append(f"Property '{path + key[2:]}' was removed")
            elif key.startswith('- ') and '+ ' + key[2:] in keys:
                formatted_val2 = format_the_value(current_value['+ ' + key[2:]])
                lines.append(f"Property '{path + key[2:]}' was updated."
                             f" From {formatted_val}"
                             f" to {formatted_val2}")

        result = itertools.chain(lines)
        return '\n'.join(result)

    return iter_(value, '')
