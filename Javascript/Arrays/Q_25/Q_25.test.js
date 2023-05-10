const subarraySort =require('./Q_25')


test('subarraySort',()=>{

    let array=[1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    expect(subarraySort(array)).toEqual([3,9])

}

)