from Q_27 import minRewards


def test_minRewards():
    #TestCase 1
    scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
    assert minRewards(scores)== 25