import itertools
from types import NoneType
import json


def boolean_to_string(dictionary):
    for key in dictionary:
        if isinstance(dictionary[key], NoneType | bool):
            dictionary[key] = json.dumps(dictionary[key])
    return dictionary


def generate_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    result = {}
    for key in keys:
        if key not in data1:
            result[f'+ {key}'] = data2[key]
        elif key not in data2:
            result[f'- {key}'] = data1[key]
        elif data1[key] == data2[key]:
            result[f'  {key}'] = data1[key]
        else:
            result[f'- {key}'] = data1[key]
            result[f'+ {key}'] = data2[key]
    return boolean_to_string(result)


def stringify(value, replacer=' ', spaces_count=1):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)
