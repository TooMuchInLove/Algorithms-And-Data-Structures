# -*- coding: utf-8 -*-

from pytest import mark
from binary_search import binary_search
from binary_search import IntArray, IndexAndCount


test_array0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
@mark.parametrize("_array, _value, _result", [
    (test_array0, 19, (-1, 0)),
    (test_array0, 13, (12, 4)),
    (test_array0, -3, (-1, 0)),
    (test_array0, "5", (-1, 0)),
    (test_array0, 13.0, (-1, 0)),
    (test_array0, 4, (3, 2)),
    (test_array0, 7.1, (-1, 0)),
])
def test_binary_search(_array: IntArray, _value: int, _result: IndexAndCount):
    result_function = binary_search(_array, _value)
    assert result_function == _result
