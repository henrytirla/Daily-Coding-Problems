"""Spiral Traverse
Write a function that takes in an n x m two-dimensional array (that can be square-shaped when n == m)
and returns a one-dimensional array of all the array's elements in spiral order.

Spiral order starts at the top left corner of the two-dimensional array,
goes to the right, and proceeds in a spiral pattern all the way until every element has been visited.

Sample Input
array = [
  [1,   2,  3, 4],
  [12, 13, 14, 5],
  [11, 16, 15, 6],
  [10,  9,  8, 7],
]
Sample Output
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]



MENTAL MODEL

When moving on the x-axis ie the horizontal line traverse columns XC for me

when moving on Y-axis ie the vertical line traverse rows  YR for me

"""
# O(n) time | O(n) space - where n is the total number of elements in the array

"Commented this diagram to aid with my visualization of solution"
# array = [
          # Startcolumn
# StartRow[1, 2,   3,   4],
#         [12, 13, 14,  5],
#         [11, 16, 15,  6],
#         [10, 9,   8,  7],
#
# ]
"""Moving in X- Axis horizontaly = Rows  XR
   Moving in Y- Axis Vertically = Columns YC
  result.append(array[what is the axis location][What is the variables location ])
  """

""


def spiralTraverse(array):

    result = []
    startRow, endRow = 0, len(array) - 1
    startColumn, endColumn = 0, len(array[0]) - 1

    while startRow <= endRow and startColumn <= endColumn:
        for col in range(startColumn, endColumn + 1):
            result.append(array[startRow][col])
        for rows in range(startRow + 1, endRow + 1):
            result.append(array[rows][endColumn])

        for col in reversed(range(startColumn, endColumn)):
            if startRow == endRow:
                break;
            result.append(array[endRow][col])

        for row in reversed(range(startRow + 1, endRow)):
            if startColumn == endColumn:
                break;

            result.append(array[row][startColumn])

        startColumn += 1
        startRow += 1
        endColumn -= 1
        endRow -= 1

    return result

array = [
  [1,   2,  3, 4],
  [12, 13, 14, 5],
  [11, 16, 15, 6],
  [10,  9,  8, 7],
]

print(spiralTraverse(array))