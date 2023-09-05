#!/usr/bin/env python3
from gendiff.cli import get_parser
from gendiff.diff_generator import generate_diff


def main():
    args = get_parser()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
