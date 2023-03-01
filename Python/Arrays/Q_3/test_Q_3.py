import pytest

from Q_3 import sortedSquaredArray


def test_sortedSquaredArray():
    #TestCase 1
    array = [-1, -2, -14, 5, 6, 8, 9]
    assert sortedSquaredArray(array) == [1, 4, 196, 25, 36, 64, 81]

