#!/usr/bin/env python3


import argparse
import json
from gendiff.diff_files.diff_json import generate_diff, stringify


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


def main():
    diff = generate_diff(first_file, second_file)
    print(stringify(diff))


if __name__ == "__main__":
    main()
