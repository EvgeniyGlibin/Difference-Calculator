#!/usr/bin/env python3


import itertools
import argparse
import json

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.'
    )
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()


first_file = json.load(open(
    '/home/user/python-project-50/gendiff/file1.json'
    ))
second_file = json.load(open(
    '/home/user/python-project-50/gendiff/file2.json'
    ))


def index_first_symbol(string):
    for i in string:
        if i.isalpha():
            index = string.index(i)
            return index


def generate_diff(file_path1, file_path2):

    diff_file = {}
    for i in file_path1:
        if i in file_path2:
            if file_path1[i] == file_path2[i]:
                diff_file[f'  {i}'] = file_path1[i]
            else:
                diff_file[f'- {i}'] = file_path1[i]
                diff_file[f'+ {i}'] = file_path2[i]
        else:
            diff_file[f'- {i}'] = file_path1[i]

    for i in file_path2:
        if i not in file_path1:
            diff_file[f'+ {i}'] = file_path2[i]

    sorted_diff_file = sorted(
        diff_file.items(), key=lambda x: x[0][index_first_symbol(x[0])]
        )
    return dict(sorted_diff_file)


def stringify(value, replacer=' ', spaces_count=1):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)


def main():
    diff = generate_diff(first_file, second_file)
    print(stringify(diff))


if __name__ == "__main__":
    main()
