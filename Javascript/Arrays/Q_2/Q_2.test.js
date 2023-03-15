
const checkSequence = require('./Q_2')

test('Find Sequence',() =>{
    expect(checkSequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])).toEqual(true)
})