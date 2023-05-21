from Q_29 import countSquares


def test_countSquares():
    points = [[1, 1],[0, 0],[-4, 2],[-2, -1], [0, 1],[1, 0],[-1, 4]
    ]
    assert countSquares(points) == 2