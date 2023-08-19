import json
import yaml
from yaml.loader import SafeLoader
from gendiff.diff_files.stylish import stringify
from gendiff.diff_files.plain import get_plain_formater
from gendiff.diff_files.gener_diff import generate_result


def generate_diff(file_path1, file_path2, format_name=stringify):
    if file_path1.endswith('.json'):
        first_file = json.load(open(file_path1))
    elif file_path1.endswith((".yaml", ".yml")):
        first_file = yaml.load(open(file_path1), Loader=SafeLoader)
    if file_path2.endswith('.json'):
        second_file = json.load(open(file_path2))
    elif file_path2.endswith((".yaml", ".yml")):
        second_file = yaml.load(open(file_path2), Loader=SafeLoader)

    result = generate_result(first_file, second_file)

    if format_name == 'stylish':
        format_name = stringify
    elif format_name == 'plain':
        format_name = get_plain_formater
    elif format_name == 'plain':
        format_name = json.dumps

    return format_name(result)
