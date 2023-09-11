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


path_file1_json = "/home/evgeniy/python-project-50/tests/fixtures/file1.json"
path_file2_json = "/home/evgeniy/python-project-50/tests/fixtures/file2.json"
first_file = json.loads(read(path_file1_json))
second_file = json.loads(read(path_file2_json))
print(generate_result(first_file, second_file))
