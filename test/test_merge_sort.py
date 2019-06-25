import pytest
from Search.merge_sort import merge_sort

def test_sorted_array():
    return_val = merge_sort([1,2,3])
    assert return_val == [1,2,3]

def test_reverse_sorted_array():
    return_val = merge_sort([3,2,1])
    assert return_val == [1,2,3]

def test_unsorted_array():
    return_val = merge_sort([2,3,1])
    assert return_val == [1,2,3]

def test_empty_array():
    return_val = merge_sort([])
    assert return_val == []

def test_negative_array():
    return_val = merge_sort([-1,-2,-3,0])
    assert return_val == [-3, -2, -1, 0]