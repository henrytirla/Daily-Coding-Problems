const minRewards = require('./Q_27')

test('minRewards',()=>{

    let scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
    expect(minRewards(scores)).toEqual(25)

})