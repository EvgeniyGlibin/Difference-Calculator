import json
import yaml
from gendiff.diff_files.formats.stylish import stringify
from gendiff.diff_files.formats.plain import get_plain_formater
from gendiff.diff_files.formats.json import get_json
from gendiff.diff_files.gener_diff import generate_result


FILE_FORMAT = {
    "json": json.loads,
    "yaml": yaml.safe_load,
    "yml": yaml.safe_load,
}

OUTPUT_FORMAT = {
    "stylish": stringify,
    "plain": get_plain_formater,
    "json": get_json,
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

    result = generate_result(parsed_file_data1, parsed_file_data2)
    return OUTPUT_FORMAT[format_name](result)
