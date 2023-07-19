import itertools


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
