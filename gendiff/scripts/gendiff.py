#!/usr/bin/env python3
from gendiff.cli import get_parser
from gendiff.diff_generator import generate_diff


args, format_name = get_parser()
# file_path1 = '/home/user/python-project-50/gendiff/file1'
# file_path2 = '/home/user/python-project-50/gendiff/file2'


# if args.first_file.endswith(".json"):
#     first_file = f'{file_path1}.json'
# elif args.first_file.endswith((".yaml", ".yml")):
#     first_file = f'{file_path1}.yaml'
# else:
#     print("Нет такого файла")

# if args.second_file.endswith(".json"):
#     second_file = f'{file_path2}.json'
# elif args.second_file.endswith((".yaml", ".yml")):
#     second_file = f'{file_path2}.yaml'
# else:
#     print("Нет такого файла")


def main():
    diff = generate_diff(args.first_file, args.second_file, format_name)
    print(diff)


if __name__ == "__main__":
    main()
