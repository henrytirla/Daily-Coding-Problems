import pytest

from Q_5 import DuplicateNum

def test_DuplicateNum():
    #Test Case1
    arr= [1,2,3,4,5,6,3]
    assert DuplicateNum(arr) == True