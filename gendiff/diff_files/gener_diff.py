import json


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
        return result


def generate_result(data1, data2):

    def iter_(current_data1, current_data2):

        keys = sorted(current_data1.keys() | current_data2.keys())
        result = []
        for key in keys:
            if key not in current_data1:
                result.append({
                    'key': key,
                    'operation': 'added',
                    'new_value': current_data2[key],
                })

            elif key not in current_data2:
                result.append({
                    'key': key,
                    'operation': 'remove',
                    'old_value': current_data1[key],
                })
            elif current_data1[key] == current_data2[key]:
                result.append({
                    'key': key,
                    'operation': 'unchanged',
                    'old_value': current_data1[key],
                })
            elif isinstance(current_data1[key], dict) is True and isinstance(
                    current_data2[key], dict) is True:
                children = iter_(current_data1[key], current_data2[key])
                result.append({
                    'key': key,
                    'operation': 'nested',
                    'new_value': children,
                })
            else:
                result.append({
                    'key': key,
                    'operation': 'changed',
                    'old_value': current_data1[key],
                    'new_value': current_data2[key],
                })

        return result

    return iter_(data1, data2)

# преобразовать создание словаря в виде key:   ,
# operation:[added, change ....], new: ..., old:...


path_file1_json = "tests/fixtures/file1.json"
path_file2_json = "tests/fixtures/file2.json"
first_file = json.loads(read(path_file1_json))
second_file = json.loads(read(path_file2_json))
nested = (generate_result(first_file, second_file))

# print('----------------------------')
# for i in x:
#     print(i, sep='\n')


data1 = {
    "follow": "false",
    "host": "hexlet.io",
    "proxy": "123.234.53.22",
    "timeout": 50,
    }

data2 = {
    "host": 'hexlet.io',
    "timeout": 20,
    "verbose": True
}

gen_diff = generate_result(data1, data2)
# print(gen_diff)

# print('-------------------')
# for dictionary in gen_diff:
#     print(dictionary)
# dictionary = gen_diff[0]
# print(dictionary)
# for key, val in dictionary.items():
#     print(key, val, sep=' -- ')
import itertools
from types import NoneType
import json


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
                val = str(dictionary['old_value'])
                lines.append(f'{deep_indent}{"- "}{key}: {val}')
            elif operation in ['unchanged']:
                val = str(dictionary['old_value'])
                lines.append(f'{deep_indent}{"  "}{key}: {val}')
            elif operation in ['added']:
                val = str(dictionary['new_value'])
                lines.append(f'{deep_indent}{"+ "}{key}: {val}')
            elif operation in ['changed']:
                old_val = str(dictionary['old_value'])
                new_val = str(dictionary['new_value'])
                lines.append(f'{deep_indent}{"- "}{key}: {old_val}')
                lines.append(f'{deep_indent}{"+ "}{key}: {new_val}')
            elif operation in ['nested']:
                val = (dictionary['new_value'])
                lines.append(f'{deep_indent}{"  "}{key}: {iter_(val, deep_indent_size)}')

        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

            # for key, val in dictionary.items():
            #     if isinstance(val, NoneType | bool):
            #         val = json.dumps(val)
            #     if str(key)[0] in "+- ":
            #         deep_indent = replacer * (deep_indent_size - 2)
            #     lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
            # result = itertools.chain("{", lines, [current_indent + "}"])
            # return '\n'.join(result)

    return iter_(value, 0)


# string = stringify(gen_diff)
# print(string)
stylish_nested = stringify(nested)
print(stylish_nested)