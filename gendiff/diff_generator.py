import json
import yaml
from gendiff.diff_files.formats.stylish import stringify
from gendiff.diff_files.formats.plain import get_plain_formater
from gendiff.diff_files.formats.json import get_json
from gendiff.diff_files.gener_diff import generate_result


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
        return result


def get_format_files(path):
    return path.split('.')[-1]


FORMATS = {
    "json": json.loads,
    "yaml": yaml.safe_load,
    "yml": yaml.safe_load,
}


def generate_diff(file_path1, file_path2, format_name='stylish'):
    first_file = FORMATS[get_format_files(file_path1)](read(file_path1))
    second_file = FORMATS[get_format_files(file_path2)](read(file_path2))

    result = generate_result(first_file, second_file)

    if format_name == 'stylish':
        format_name = stringify
    elif format_name == 'plain':
        format_name = get_plain_formater
    elif format_name == 'json':
        format_name = get_json

    return format_name(result)
