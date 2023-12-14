"""Given an n x n square matrix, write a program to rotate the matrix by 90 degrees in the anti-clockwise direction. The goal is to perform the matrix rotation in place, meaning we need to rotate the matrix without using extra space.

Example 1:[1, 2, 3        =>      [1, 4, 7,
             4, 5, 6                2, 5, 8,
              7, 8, 9]               3, 6, 9]




"""

# Visualize execution
# https://pythontutor.com/render.html#code=def%20transposeMatrix%28matrix%29%3A%0A%20%20%20%20transposeMatrix%20%3D%5B%5D%0A%20%20%20%20for%20col%20in%20range%28len%28matrix%5B0%5D%29%29%3A%0A%20%20%20%20%20%20%20%20newRow%3D%20%5B%5D%0A%20%20%20%20%20%20%20%20for%20row%20in%20range%28len%28matrix%29%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20newRow.append%28matrix%5Brow%5D%5Bcol%5D%29%0A%20%20%20%20%20%20%20%20transposeMatrix.append%28newRow%29%0A%20%20%20%20return%20transposeMatrix%0A%20%20%20%20%0A%20%20%20%20%0Amatrix%3D%20%5B%5B1,%202,%203%5D,%20%5B4,%205,%206%5D,%20%5B7,%208,%209%5D%5D%0A%0Aprint%28transposeMatrix%28matrix%29%29&cumulative=false&curInstr=38&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
def test_rotateMatrix():
    sol = Solution()

    assert sol.transposeMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
    ]
    assert sol.transposeMatrix([[1, 2, 3, 4, 5, 6]]) == [[1], [2], [3], [4], [5], [6]]


class Solution:
    def transposeMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        transposeMatrix = []
        for col in range(len(matrix[0])):
            newRow = []
            for row in range(len(matrix)):
                newRow.append(matrix[row][col])
            transposeMatrix.append(newRow)
        return transposeMatrix
