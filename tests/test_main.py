import pytest

def create_dict(keys, values):
    return dict(zip(keys, values))

def test_create_dict():
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    expected = {'a': 1, 'b': 2, 'c': 3}
    assert create_dict(keys, values) == expected

def test_create_dict_unequal_length():
    keys = ['a', 'b', 'c']
    values = [1, 2]
    expected = {'a': 1, 'b': 2}
    assert create_dict(keys, values) == expected

def test_create_dict_empty():
    keys = []
    values = []
    expected = {}
    assert create_dict(keys, values) == expected

def test_create_dict_single_element():
    keys = ['a']
    values = [1]
    expected = {'a': 1}
    assert create_dict(keys, values) == expected
