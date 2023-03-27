from Q_19 import firstDuplicateValue

def test_firstDuplicateValue():
    arr=[2,1,5,3,3,2,4]
    assert firstDuplicateValue(arr)== 3
    #Testcase 2
    arr =[2,1,5,2,3,3,4]
    assert firstDuplicateValue(arr) == 2