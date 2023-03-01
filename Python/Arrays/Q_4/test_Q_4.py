import pytest

from Q_4 import products


def test_products():
    #Test Case 1
    arr= [1, 2, 3, 4,5]
    assert products(arr) == [120, 60, 40, 30, 24]