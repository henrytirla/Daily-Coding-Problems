import pytest

from Q_10 import teamWinner

def test_teamWinner():
    #TestCase 1
    matches = [
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"],
    ]

    results = (0, 0, 1)

    assert(teamWinner(matches,results)) == "Python"