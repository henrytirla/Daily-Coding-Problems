const countSquares = require('./Q_29')


test('countSquares',()=>{
    let points = [[1, 1], [0, 0], [-4, 2], [-2, -1], [0, 1], [1, 0], [-1, 4]]
    expect(countSquares(points)).toEqual(2)
})