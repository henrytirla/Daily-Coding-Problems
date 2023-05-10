from Q_25 import subarraySort

def test_subarraySort():
    #TestCase 1

    array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    assert(subarraySort(array)) == [3,9]
