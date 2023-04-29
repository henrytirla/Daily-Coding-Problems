const missingNumbers = require('./Q_23')

test('missingNumbers',()=>{
    let nums =[1,4,3]
    expect(missingNumbers(nums)).toEqual([2,5])
})