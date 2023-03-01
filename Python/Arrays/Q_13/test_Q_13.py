import pytest
from Q_13 import find_closest_pair

def test_find_closest_pair():
    arrayOne = [-1, 5, 10, 20, 28, 3]
    arrayTwo = [26, 134, 135, 15, 17]

    assert(find_closest_pair(arrayOne,arrayTwo)) == [28, 26]
