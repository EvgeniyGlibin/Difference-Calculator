#!/usr/bin/env python3


import argparse
import json
from gendiff.diff_files.formats.stylish import stringify
from gendiff.diff_files.formats.plain import get_plain_formater


def get_parser():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish',
                        help='set format of output')
    args = parser.parse_args()
    if args.format == 'stylish':
        format_name = stringify
    elif args.format == 'plain':
        format_name = get_plain_formater
    elif args.format == 'json':
        format_name = json.dumps

    return args, format_name


def main():
    get_parser()


if __name__ == "__main__":
    main()
