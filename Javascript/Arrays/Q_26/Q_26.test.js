const largestRange = require('./Q_26')


test('largestRange',()=>{
    let array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6];

    expect(largestRange(array)).toEqual([0,7])
})