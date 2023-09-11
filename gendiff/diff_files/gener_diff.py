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
                # result[f'+ {key}'] = current_data2[key]
                result.append({
                    'key': key,
                    'type_operation': 'added',
                    'new_value': current_data2[key],
                })

            elif key not in current_data2:
                # result[f'- {key}'] = current_data1[key]
                result.append({
                    'key': key,
                    'type_operation': 'remove',
                    'old_value': current_data1[key],
                })
            elif current_data1[key] == current_data2[key]:
                # result[f'  {key}'] = current_data1[key]
                result.append({
                    'key': key,
                    'type_operation': 'unchanged',
                    'old_value': current_data1[key],
                })
            elif isinstance(current_data1[key], dict) is True and isinstance(
                    current_data2[key], dict) is True:
                children = iter_(current_data1[key], current_data2[key])
                # result[f'  {key}'] = children
                result.append({
                    'key': key,
                    'type_operation': 'nested',
                    'new_value': children,
                })
            else:
                # result[f'- {key}'] = current_data1[key]
                # result[f'+ {key}'] = current_data2[key]
                result.append({
                    'key': key,
                    'type_operation': 'changed',
                    'old_value': current_data1[key],
                    'new_value': current_data2[key],
                })

        return result

    return iter_(data1, data2)

# преобразовать создание словаря в виде key:   ,
# type_operation:[added, change ....], new: ..., old:...


# path_file1_json = "/home/evgeniy/python-project-50/tests/fixtures/file1.json"
# path_file2_json = "/home/evgeniy/python-project-50/tests/fixtures/file2.json"
# first_file = json.loads(read(path_file1_json))
# second_file = json.loads(read(path_file2_json))
# x = (generate_result(first_file, second_file))

# print('----------------------------')
# for i in x:
#     print(i, sep='\n')


data1 = {
    "follow": False,
    "host": "hexlet.io",
    "proxy": "123.234.53.22",
    "timeout": 50,
    }

data2 = {
    "host": 'hexlet.io',
    "proxy": "123.234.53.45",
    "timeout": 25,
    "promt": True
}

gen_diff = generate_result(data1, data2)
print(gen_diff)
print('-------------------')
# dictionary = gen_diff[0]
# print(dictionary)
# for key, val in dictionary.items():
#     print(key, val, sep=' -- ')
import itertools
from types import NoneType
import json


def stringify(value, replacer=' ', spaces_count=4):

    def iter_(current_value, depth):
        for dictionary in current_value:
            if not isinstance(dictionary, dict):
                return str(dictionary)

            deep_indent_size = depth + spaces_count
            deep_indent = replacer * deep_indent_size
            current_indent = replacer * depth
            lines = []
            key = dictionary['key']
            val = str(dictionary['old_value'])
            if dictionary['type_operation'] in ['added', 'remove', 'changed', 'unchanged']:
                deep_indent = replacer * (deep_indent_size - 2)
                lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
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


string = stringify(gen_diff)
print(string)