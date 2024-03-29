/**
 Zigzag Traverse
 Write a function that takes in an n x m two-dimensional array
 (that can be square-shaped when n == m) and returns a one-dimensional
 array of all the array's elements in zigzag order.

 Zigzag order starts at the top left corner of the
 two-dimensional array, goes down by one element, and proceeds
 in a zigzag pattern all the way to the bottom right corner.

 Sample Input
 array = [
 [1,  3,  4, 10],
 [2,  5,  9, 11],
 [6,  8, 12, 15],
 [7, 13, 14, 16],
 ]
 Sample Output
 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
 */


function zigzagTraverse(array) {
    let height = array.length - 1;
    let width = array[0].length - 1;
    let result = [];
    let row = 0, col = 0;
    let goingDown = true;

    while (!isOutOfBounds(row, col, height, width)) {
        result.push(array[row][col]);

        if (goingDown) {
            if (col == 0 || row == height) {
                goingDown = false;
                if (row == height) {
                    col += 1;
                } else {
                    row += 1;
                }
            } else {
                row += 1;
                col -= 1;
            }
        } else {
            if (row == 0 || col == width) {
                goingDown = true;
                if (col == width) {
                    row += 1;
                } else {
                    col += 1;
                }
            } else {
                row -= 1;
                col += 1;
            }
        }
    }

    return result;
}

function isOutOfBounds(row, col, height, width) {
    return row < 0 || row > height || col < 0 || col > width;
}


let array = [
    [1,  3,  4, 10],
    [2,  5,  9, 11],
    [6,  8, 12, 15],
    [7, 13, 14, 16],
]
console.log(zigzagTraverse(array))

module.exports = zigzagTraverse;