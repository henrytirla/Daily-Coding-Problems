from Q_28 import zigzagTraverse


def test_zigzagTraverse():
    #TestCase1
    array = [
        [1, 3, 4, 10],
        [2, 5, 9, 11],
        [6, 8, 12, 15],
        [7, 13, 14, 16],]
    assert(zigzagTraverse(array)) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
