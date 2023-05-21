"""Count Squares
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
// as does [1, 1], [-4, 2], [-2, -1], and [-1, 4]"""


import math

def countSquares(points):
    points = set(tuple(point) for point in points)
    squares = 0

    for (x1, y1) in points:
        for (x2, y2) in points:
            if (x1, y1) != (x2, y2):
                dx = x2 - x1
                dy = y2 - y1

                # Calculate the coordinates of the two other points.
                x3, y3 = x1 - dy, y1 + dx
                x4, y4 = x2 - dy, y2 + dx

                # If those points are in our input list, we have a square.
                if (x3, y3) in points and (x4, y4) in points:
                    squares += 1

    # Each square is counted four times in the loops (once for each corner),
    # so we divide the total count by 4.
    return squares // 4

if __name__ == '__main__':

    points = [
      [1, 1],
      [0, 0],
      [-4, 2],
      [-2, -1],
      [0, 1],
      [1, 0],
      [-1, 4]
    ]

    print(countSquares(points))
