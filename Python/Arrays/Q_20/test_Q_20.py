from Q_20 import mergeOverlappingIntervals



def test_mergeOverlappingIntervals():
    #TestCase 1
    arr= [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
    assert mergeOverlappingIntervals(arr) == [[1, 2], [3, 8], [9, 10]]

    #TestCase 2
