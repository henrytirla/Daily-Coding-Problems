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

def zigZag(array):
    height= len(array)-1
    width = len(array[0])
    result = []
    row,col = 0,0
    goingDown = True
    while not isOutOfBounds(row,col,height,width):
              if goingDown:
                  if col==0 and row == height:
                      goingDown= False
                      if row == height:
                         col+=1
                      else:
                         row+=1
                  else:
                      row+=1
                      col-=1
                  if row==0 and col == width:
                      goingDown = True
                      if col == width:
                         row+=1
                      else:
                          col+=1
                  else:
                      row-=1
                      col+=1
    return result









def isOutOfBounds(array):
    return row< 0 or row>height or col <0 or col>height
