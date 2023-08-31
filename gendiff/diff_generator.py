import json
import yaml
from yaml.loader import SafeLoader
from gendiff.diff_files.formats.stylish import stringify
from gendiff.diff_files.formats.plain import get_plain_formater
from gendiff.diff_files.formats.json import get_json
from gendiff.diff_files.gener_diff import generate_result


def get_path(data):
    if data.endswith('.json'):
        result = json.loads(f"{data}")
    elif data.endswith((".yaml", ".yml")):
        result = yaml.load(data, Loader=SafeLoader)
    return result


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
        return result

# https://stackoverflow.com/questions/16573332/jsondecodeerror-expecting-value-line-1-column-1-char-0

def generate_diff(file_path1, file_path2, format_name='stylish'):
    first_file = read(get_path(file_path1))
    second_file = read(get_path(file_path2))

    result = generate_result(first_file, second_file)

    if format_name == 'stylish':
        format_name = stringify
    elif format_name == 'plain':
        format_name = get_plain_formater
    elif format_name == 'json':
        format_name = get_json

    return format_name(result)
