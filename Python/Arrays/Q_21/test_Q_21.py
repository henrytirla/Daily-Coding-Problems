from Q_21 import bestSeat

def test_bestSeat():

    #TestCase1
    seat = [1, 0, 1, 0, 0, 0, 1]
    assert bestSeat(seat)== 4
    #TestCase2
    seat2= [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
    assert bestSeat(seat) == 4
