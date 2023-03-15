

// const twoNum = require('./');
//
// test('Finds two numbers that adds to trarget sum',() => {
//     expect(twoNumberSum([5, 1n, 22, 25, 6, -1, 8, 10],23).toBe(1,yar22));
// })

const twoNumberSum = require('./Q_1');

test('Finds two numbers that add to target sum', () => {
    expect(twoNumberSum([5, 1, 22, 25, 6, -1, 8, 10], 23)).toEqual([1, 22]);
});