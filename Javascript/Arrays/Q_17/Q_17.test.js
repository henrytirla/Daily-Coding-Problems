const longest_peak = require('./Q_17');

test('Finds Longest Peak', () => {
    expect(longest_peak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3])).toEqual(6);
});