import pytest
from Q_1 import twoNumberSum

def test_twoNumberSum():
    # Test case 1
    arr = [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10
    assert twoNumberSum(arr, targetSum) == (-1,11)

    # Test Case 2
    arr = [4, 6]
    targetSum = 10
    assert twoNumberSum(arr, targetSum) == (6,4)

    # Test Case 3
    arr = [4,6,1]
    targetSum = 5
    assert twoNumberSum(arr, targetSum) == (1, 4)

    # Test Case 4
    arr = [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47]
    targetSum = 163
    assert twoNumberSum(arr, targetSum) == (-47, 210)