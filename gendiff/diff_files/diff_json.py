import itertools
from types import NoneType
import json


def stringify(value, replacer=' ', spaces_count=4):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            if isinstance(val, NoneType | bool):
                val = json.dumps(val)
            if str(key)[0] in "+- ":
                deep_indent = replacer * (deep_indent_size - 2)
            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)


def generate_diff(data1, data2):

    def iter_(current_data1, current_data2):

        keys = sorted(current_data1.keys() | current_data2.keys())
        result = {}
        for key in keys:
            if key not in current_data1:
                result[f'+ {key}'] = current_data2[key]
            elif key not in current_data2:
                result[f'- {key}'] = current_data1[key]
            elif current_data1[key] == current_data2[key]:
                result[f'  {key}'] = current_data1[key]
            elif isinstance(current_data1[key], dict) is True and isinstance(
                    current_data2[key], dict) is True:
                children = iter_(current_data1[key], current_data2[key])
                result[f'  {key}'] = children
            else:
                result[f'- {key}'] = current_data1[key]
                result[f'+ {key}'] = current_data2[key]

        return result

    return iter_(data1, data2)
