/**
 Count Squares
 Write a function that takes in a list of Cartesian coordinates (i.e., (x, y) coordinates)
 and returns the number of squares that can be formed by these coordinates.

 A square must have its four corners amongst the coordinates in order to be counted.
 A single coordinate can be used as a corner for multiple different squares.

 You can also assume that no coordinate will be farther than 100 units from the origin.

 Sample Input
 points = [
 [1, 1],
 [0, 0],
 [-4, 2],
 [-2, -1],
 [0, 1],
 [1, 0],
 [-1, 4]
 ]
 Sample Output
 2  // [1, 1], [0, 0], [0, 1], and [1, 0] makes a square,
 // as does [1, 1], [-4, 2], [-2, -1], and [-1, 4]
 */

function countSquares(points) {
    let squares = 0;
    let pointSet = new Set(points.map(JSON.stringify));

    for (let [x1, y1] of points) {
        for (let [x2, y2] of points) {
            if (x1 !== x2 || y1 !== y2) {
                let dx = x2 - x1;
                let dy = y2 - y1;

                let x3 = x1 - dy;
                let y3 = y1 + dx;
                let x4 = x2 - dy;
                let y4 = y2 + dx;

                if (pointSet.has(JSON.stringify([x3, y3])) && pointSet.has(JSON.stringify([x4, y4]))) {
                    squares++;
                }
            }
        }
    }

    return squares / 4;
}

// Testing
let points = [
    [1, 1],
    [0, 0],
    [-4, 2],
    [-2, -1],
    [0, 1],
    [1, 0],
    [-1, 4]
];

console.log(countSquares(points));  // Outputs: 2
module.exports=countSquares;