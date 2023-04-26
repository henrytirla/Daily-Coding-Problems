const mergeOverlappingIntervals = require('./Q_20')

test('MergeOverlappingIntervals',() =>{

    expect(mergeOverlappingIntervals([[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]])).toEqual([ [ 1, 2 ], [ 3, 8 ], [ 9, 10 ] ]
    )

    //TestCase 2

})