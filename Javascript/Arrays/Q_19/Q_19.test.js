const firstDuplicateValue= require('./Q_19')

test('FirstDuplicate',() =>{

    expect(firstDuplicateValue([2,1,5,3,3,2,4])).toEqual(3)

    //TestCase 2
    expect(firstDuplicateValue([2,1,5,2,3,3,4])).toEqual(2)
})