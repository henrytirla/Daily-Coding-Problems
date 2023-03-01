import pytest

from Q_11 import nonConstructibleChange

def test_nonConstructibleChange():
    #TestCase 1
    coins = [1, 2, 5]
    assert(nonConstructibleChange(coins))== 4

    #TestCase 2
    coins2 = [5, 7, 1, 1, 2, 3, 22]
    assert(nonConstructibleChange(coins2)) == 20


