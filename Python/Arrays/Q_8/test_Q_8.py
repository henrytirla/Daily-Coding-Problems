import pytest

from Q_8 import MostFrequent

def test_MostFrequent():
    # TestCase 1
    nums = [1,1,2,2,2,3]
    k = 2
    assert(MostFrequent(nums,k)) == [2,1]

