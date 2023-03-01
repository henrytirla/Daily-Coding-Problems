import pytest

from Q_6 import checkAnagram

def test_checkAnagram():
    #Test Case 1
    s = "anagram"
    t = "nagaram"
    assert checkAnagram(s,t) == True

    #Test Case 2
    s= "Henry"
    t= "Tirla"
    assert checkAnagram(s,t) == False