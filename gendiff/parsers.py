import json
import yaml
from gendiff.diff_files.formats.stylish import get_stylish_format
from gendiff.diff_files.formats.plain import get_plain_format
from gendiff.diff_files.formats.json import get_json_format
from gendiff.diff_files.difference_tree import get_diff_tree


FILE_FORMAT = {
    "json": json.loads,
    "yaml": yaml.safe_load,
    "yml": yaml.safe_load,
}

OUTPUT_FORMAT = {
    "stylish": get_stylish_format,
    "plain": get_plain_format,
    "json": get_json_format,
}


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
        return result


def get_file_extension(path):
    return path.split('.')[-1]


def generate_diff(file_path1, file_path2, format_name='stylish'):
    parsed_file_data1 = FILE_FORMAT[get_file_extension(file_path1)](
        read(file_path1)
    )
    parsed_file_data2 = FILE_FORMAT[get_file_extension(file_path2)](
        read(file_path2)
    )

    result = get_diff_tree(parsed_file_data1, parsed_file_data2)
    return OUTPUT_FORMAT[format_name](result)
