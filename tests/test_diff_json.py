from gendiff.diff_files.diff_json import index_first_symbol
from gendiff.diff_files.diff_json import generate_diff
from gendiff.diff_files.diff_json import stringify
from gendiff.diff_files.diff_json import boolean_to_string
import os


file1 = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
  }


file2 = {
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io"
  }


primitives = {
    "string": "value",
    "boolean": True,
    "number": 5,
}


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


def test_index_first_symbol():
    assert index_first_symbol('+ Hexlet') == 2
    assert index_first_symbol(' -  eXlet') == 4


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


plain_data = read(get_fixture_path('plain.txt')).rstrip().split('\n\n\n')
nested_data = read(get_fixture_path('nested.txt')).rstrip().split('\n\n\n')
gen_diff = generate_diff(file1, file2)
flat_json_1 = read(get_fixture_path('flat_json.txt')).rstrip().split('\n\n\n')


def test_default_values():
    assert stringify(primitives) == plain_data[2]
    assert stringify(primitives, '|-') == plain_data[0]
    assert stringify(primitives, '|-', 2) == plain_data[1]
    assert stringify(nested) == nested_data[1]
    assert stringify(nested, ' ') == nested_data[1]
    assert stringify(nested, '...') == nested_data[0]
    assert stringify(nested, '|-', 2) == nested_data[2]
    assert stringify(gen_diff) == flat_json_1[0]


def test_generate_diff():
    assert generate_diff(file1, file2) == {
        '- follow': 'false',
        '  host': 'hexlet.io',
        '- proxy': '123.234.53.22',
        '- timeout': 50,
        '+ timeout': 20,
        '+ verbose': 'true',
        }


def test_boolean_to_string():
    assert boolean_to_string(primitives) == {
        "string": "value",
        "boolean": "true",
        "number": 5,
        }
    assert boolean_to_string(file1) == {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": "false",
        }
    assert boolean_to_string({"a": 1, "b": "aa"}) == {
        "a": 1,
        "b": "aa",
        }
