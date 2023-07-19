from gendiff.diff_files.diff_json import index_first_symbol
import pytest


def test_index_first_symbol():
    assert index_first_symbol('+ Hexlet') == 2
    assert index_first_symbol(' -  eXlet') == 4


# def test_reverse_for_empty_string():
#     assert reverse('') == ''


print('Тесты работают')