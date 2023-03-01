import pytest

from Q_15 import isMonotonic

def test_isMonotonic():
    #TestCase 1
    array = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11]
    assert (isMonotonic(array))== False