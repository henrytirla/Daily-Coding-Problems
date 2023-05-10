const FourNumberSums = require('./Q_24')


test('FourNumberSums',()=> {

    let array= [7, 6, 4, -1, 1, 2]
    let targetNum= 16
    expect(FourNumberSums(array,targetNum)).toEqual([ [ 7, 6, 4, -1 ], [ 7, 6, 1, 2 ] ]
    )
})