import pytest
from Q_2 import checkSequenc


def test_checkSequenc():
    #Test Case 1
    arr = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    assert checkSequenc(arr, sequence) == True