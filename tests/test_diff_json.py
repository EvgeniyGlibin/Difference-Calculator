
from gendiff.diff_files.stylish import stringify
from gendiff.diff_files.plain import get_plain_formater
from gendiff.diff_generator import generate_diff
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


file3 = {
    "common": {
        "setting1": "Value 1",
        "setting2": 200,
        "setting3": True,
        "setting6": {
            "key": "value",
            "doge": {
                "wow": "",
            }
        }
    },
    "group1": {
        "baz": "bas",
        "foo": "bar",
        "nest": {
            "key": "value",
        }
    },
    "group2": {
        "abc": 12345,
        "deep": {
            "id": 45,
        }
    }
}


file4 = {
    "common": {
        "follow": False,
        "setting1": "Value 1",
        "setting3": None,
        "setting4": "blah blah",
        "setting5": {
            "key5": "value5",
        },
        "setting6": {
            "key": "value",
            "ops": "vops",
            "doge": {
                "wow": "so much",
            }
        }
    },
    "group1": {
        "foo": "bar",
        "baz": "bars",
        "nest": "str",
    },
    "group3": {
        "deep": {
            "id": {
                "number": 45,
            }
        },
        "fee": 100500,
    }
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


file_diff = {
    "- follow": "false",
    "  host": "hexlet.io",
    "- proxy": "123.234.53.22",
    "- timeout": 50,
    "+ timeout": 20,
    "+ verbose": True,
}


plain = "Property 'follow' was removed\n" \
    "Property 'proxy' was removed\n" \
    "Property 'timeout' was updated. From 50 to 20\n" \
    "Property 'verbose' was added with value: true" \


plain_nested = "Property 'common.follow' was added with value: false\n" \
    "Property 'common.setting2' was removed\n" \
    "Property 'common.setting3' was updated. From true to null\n" \
    "Property 'common.setting4' was added with value: 'blah blah'\n" \
    "Property 'common.setting5' was added with value: [complex value]\n" \
    "Property 'common.setting6.doge.wow' was updated. From '' to 'so much'\n" \
    "Property 'common.setting6.ops' was added with value: 'vops'\n" \
    "Property 'group1.baz' was updated. From 'bas' to 'bars'\n" \
    "Property 'group1.nest' was updated. From [complex value] to 'str'\n" \
    "Property 'group2' was removed\n" \
    "Property 'group3' was added with value: [complex value]" \



def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


plain_data = read(get_fixture_path('plain.txt')).rstrip().split('\n\n\n')
nested_data = read(get_fixture_path('nested.txt')).rstrip().split('\n\n\n')
flat_json_1 = read(get_fixture_path('flat_json.txt')).rstrip().split('\n\n\n')





def test_default_values():
    assert stringify(primitives) == plain_data[2]
    assert stringify(primitives, '|-') == plain_data[0]
    assert stringify(primitives, '|-', 2) == plain_data[1]
    assert stringify(nested, ' ', 1) == nested_data[1]
    assert stringify(nested, '...', 1) == nested_data[0]
    assert stringify(nested, '|-', 2) == nested_data[2]


def test_get_plain_formater():
    assert get_plain_formater(file_diff) == plain


file_path_json1 = get_fixture_path('file1.json')
file_path_json2 = get_fixture_path('file2.json')
file_path_yaml1 = get_fixture_path('file1.yaml')
file_path_yaml2 = get_fixture_path('file2.yaml')
result_stylish = read(get_fixture_path('result_stylish'))
result_plain = read(get_fixture_path('result_plain'))


def test_generate_diff():
    assert generate_diff(file_path_json1,
                         file_path_json2, stringify) == result_stylish
    assert generate_diff(file_path_yaml1,
                         file_path_yaml2) == result_stylish
    assert generate_diff(file_path_yaml1,
                         file_path_yaml2, 'stylish') == result_stylish
    assert generate_diff(file_path_json1,
                         file_path_yaml2, get_plain_formater) == result_plain
    assert generate_diff(file_path_yaml1,
                         file_path_yaml2, 'plain') == result_plain
