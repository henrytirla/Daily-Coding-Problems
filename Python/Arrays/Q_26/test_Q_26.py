from Q_26 import largestRange

def test_largestRange():
    array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
    assert largestRange(array) == [0,7]