import pytest

from Q_17 import longest_peak

def test_longest_peak():
    arr3 = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    assert(longest_peak(arr3)) == [0, 10, 6]

    
