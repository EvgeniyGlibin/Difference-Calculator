#!/usr/bin/env python3


import argparse
import json
from gendiff.diff_files.diff_json import generate_diff, stringify
import yaml
from yaml.loader import SafeLoader

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.'
    )
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()


if args.first_file.endswith(".json"):
    first_file = json.load(open(
        '/home/user/python-project-50/gendiff/file1.json'
        ))
elif args.first_file.endswith((".yaml", ".yml")):
    first_file = yaml.load(open(
        '/home/user/python-project-50/gendiff/file11.yaml'), Loader=SafeLoader
        )
else:
    print("Нет такого файла")


if args.second_file.endswith(".json"):
    second_file = json.load(open(
        '/home/user/python-project-50/gendiff/file2.json'
        ))
elif args.second_file.endswith((".yaml", ".yml")):
    second_file = yaml.load(open(
        '/home/user/python-project-50/gendiff/file22.yaml'), Loader=SafeLoader
        )
else:
    print("Нет такого файла")


def main():
    diff = generate_diff(first_file, second_file)
    print(stringify(diff))


if __name__ == "__main__":
    main()
