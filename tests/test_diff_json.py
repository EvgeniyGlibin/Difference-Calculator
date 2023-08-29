
from gendiff.diff_files.stylish import stringify
from gendiff.diff_files.plain import get_plain_formater
from gendiff.diff_generator import generate_diff
import os
import pytest


nested = {
    "string": "value",
    "boolean": True,
    "number": 5,
    "dict": {
        5: "number",
        None: "None",
        True: "boolean",
        "value": "string",
        "nested": {
            "boolean": True,
            "string": 'value',
            "number": 5,
            None: "None",
        },
    },
}


file_diff = {
    "- follow": "false",
    "  host": "hexlet.io",
    "- proxy": "123.234.53.22",
    "- timeout": 50,
    "+ timeout": 20,
    "+ verbose": True,
}


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


nested_data = read(get_fixture_path('nested.txt')).rstrip().split('\n\n\n')

cases = [
    ('.', 3, 0),
    (' ', 1, 1),
    ('|-', 2, 2),
]


@pytest.mark.parametrize("replacer, space_count, case_index", cases)
def test_stringify(replacer, space_count, case_index):
    expected = nested_data[case_index]
    assert stringify(nested, replacer, space_count) == expected


plain_data = read(get_fixture_path('plain'))


def test_get_plain_formater():
    assert get_plain_formater(file_diff) == plain_data


file_path_json1 = get_fixture_path('file1.json')
file_path_json2 = get_fixture_path('file2.json')
file_path_yaml1 = get_fixture_path('file1.yaml')
file_path_yaml2 = get_fixture_path('file2.yaml')
result_stylish = read(get_fixture_path('result_stylish'))
result_plain = read(get_fixture_path('result_plain'))


formats = [
    (file_path_json1, file_path_json2, 'stylish', 0),
    (file_path_json1, file_path_yaml2, 'plain', 1),
    (file_path_yaml1, file_path_yaml2, 'stylish', 1),
]
result_format = [result_stylish, result_plain, result_stylish]


@pytest.mark.parametrize('file_path1, file_path2, format, format_index',
                         formats,
                         )
def test_generate_diff(file_path1, file_path2, format, format_index):
    result = result_format[format_index]
    assert generate_diff(file_path1, file_path2, format) == result
