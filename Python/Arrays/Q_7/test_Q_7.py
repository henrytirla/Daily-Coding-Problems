
import pytest
from Q_7 import GroupAnagram

def test_GroupAnagram():
    #Test Case 1
    str = ["eat","tea","tan","ate","nat","bat"]
    assert list(GroupAnagram(str)) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
