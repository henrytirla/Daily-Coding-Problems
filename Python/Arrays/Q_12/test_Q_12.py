import pytest

from Q_12 import find_tripplets

def test_find_tripplets():
    #TestCase 1
    arr = [12, 3, 1, 2, -6, 5, -8, 6]
    targetSum = 0
    assert(find_tripplets(arr,targetSum)) == [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

