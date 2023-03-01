import pytest

from Q_14 import Move_element

def test_Move_element():
    #TestCase 1
    array = [2, 1, 2, 2, 2, 3, 4, 2]
    toMove = 2
    assert(Move_element(array,toMove)) == [1, 3, 4, 2, 2, 2, 2, 2]
