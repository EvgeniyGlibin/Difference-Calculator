import itertools
from types import NoneType
import json


def to_string(value, depth, spaces_count):
    if isinstance(value, NoneType | bool):
        return json.dumps(value)
    if isinstance(value, dict):
        replacer = ' '
        current_depth = depth + spaces_count
        current_deep_indent = replacer * current_depth
        previous_deep_indent = replacer * depth
        result = '{'
        for key, val in value.items():
            result += f'\n{current_deep_indent}{key}: {to_string(val, current_depth, spaces_count)}'
        result += f'\n{previous_deep_indent}'
        result += '}'
        return result
    return str(value)


def stringify(value, replacer=' ', spaces_count=4):

    def iter_(current_value, depth):
        lines = []
        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        for dictionary in current_value:
            if not isinstance(dictionary, dict):
                return str(dictionary)

            key = dictionary['key']
            operation = dictionary['operation']
            if operation in ['added', 'unchanged', 'changed', 'nested', 'remove']:
                deep_indent = replacer * (deep_indent_size - 2)
            if operation in ['remove']:
                val = to_string(dictionary['old_value'], deep_indent_size, spaces_count)
                lines.append(f'{deep_indent}{"- "}{key}: {val}')
            elif operation in ['unchanged']:
                val = to_string(dictionary['old_value'], deep_indent_size, spaces_count)
                lines.append(f'{deep_indent}{"  "}{key}: {val}')
            elif operation in ['added']:
                val = to_string(dictionary['new_value'], deep_indent_size, spaces_count)
                lines.append(f'{deep_indent}{"+ "}{key}: {val}')
            elif operation in ['changed']:
                old_val = to_string(dictionary['old_value'], deep_indent_size, spaces_count)
                new_val = to_string(dictionary['new_value'], deep_indent_size, spaces_count)
                lines.append(f'{deep_indent}{"- "}{key}: {old_val}')
                lines.append(f'{deep_indent}{"+ "}{key}: {new_val}')
            elif operation in ['nested']:
                val = dictionary['new_value']
                lines.append(f'{deep_indent}{"  "}{key}: {iter_(val, deep_indent_size)}')

        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)
