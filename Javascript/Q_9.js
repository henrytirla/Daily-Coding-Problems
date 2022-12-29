/**
 """
 Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
 validated according to the following rules:

 Each row must contain the digits 1-9 without repetition.
 Each column must contain the digits 1-9 without repetition.
 Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
 Note:

 A Sudoku board (partially filled) could be valid but is not necessarily solvable.
 Only the filled cells need to be validated according to the mentioned rules.


 Example 1:


 Input: board =
 [["5","3",".",".","7",".",".",".","."]
 ,["6",".",".","1","9","5",".",".","."]
 ,[".","9","8",".",".",".",".","6","."]
 ,["8",".",".",".","6",".",".",".","3"]
 ,["4",".",".","8",".","3",".",".","1"]
 ,["7",".",".",".","2",".",".",".","6"]
 ,[".","6",".",".",".",".","2","8","."]
 ,[".",".",".","4","1","9",".",".","5"]
 ,[".",".",".",".","8",".",".","7","9"]]
 Output: true
 Example 2:

 Input: board =
 [["8","3",".",".","7",".",".",".","."]
 ,["6",".",".","1","9","5",".",".","."]
 ,[".","9","8",".",".",".",".","6","."]
 ,["8",".",".",".","6",".",".",".","3"]
 ,["4",".",".","8",".","3",".",".","1"]
 ,["7",".",".",".","2",".",".",".","6"]
 ,[".","6",".",".",".",".","2","8","."]
 ,[".",".",".","4","1","9",".",".","5"]
 ,[".",".",".",".","8",".",".","7","9"]]
 Output: false
 Explanation: Same as Example 1,

 except with the 5 in the top left corner being modified to 8.
 Since there are two 8's in the top left 3x3 sub-box, it is invalid.


 Constraints:

 board.length == 9
 board[i].length == 9
 board[i][j] is a digit 1-9 or '.'.

 https://leetcode.com/problems/valid-sudoku/



 Solution Explanation
 https://www.youtube.com/watch?v=TjFXEUCMqI8&t=1s
 """
 */


let board= [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]

let board2=[["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]


function ValidSudoku(board) {
    const cols = new Map();
    const rows = new Map();
    const squareChecks = new Map();

    for (let r = 0; r < 9; r++) {
        for (let c = 0; c < 9; c++) {
            if (board[r][c] === '.') continue;
            if (cols.get(c) && cols.get(c).has(board[r][c])) return false;
            if (rows.get(r) && rows.get(r).has(board[r][c])) return false;
            if (squareChecks.get(`${r/3},${c/3}`) && squareChecks.get(`${r/3},${c/3}`).has(board[r][c])) return false;

            if (!cols.get(c)) cols.set(c, new Set());
            cols.get(c).add(board[r][c]);
            if (!rows.get(r)) rows.set(r, new Set());
            rows.get(r).add(board[r][c]);
            if (!squareChecks.get(`${r/3},${c/3}`)) squareChecks.set(`${r/3},${c/3}`, new Set());
                squareChecks.get(`${r/3},${c/3}`).add(board[r][c]);
                }
  }

  return true;
}



console.log(ValidSudoku(board))