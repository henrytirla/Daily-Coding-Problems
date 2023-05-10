from Q_24 import four_number_sum

def test_four_number_sum():
    #TestCase 1
    array= [7, 6, 4, -1, 1, 2]
    targetNum= 16
    assert four_number_sum(array,targetNum)== [[7, 6, 4, -1], [7, 6, 1, 2]]

    #TestCase 2

    array2=[1, 2, 3, 4, 5, 6, 7]
    targetNum2=10
    assert  four_number_sum(array2,targetNum2)== [[1, 2, 3, 4]]