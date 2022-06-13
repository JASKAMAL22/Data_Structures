'''
STATEMENT:
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
-------------------------------------------------
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(i):
            if i == n:
                res.append(list(board))
            for j in range(n):
                if j not in cols and j-i not in diag and j+i not in off_diag:
                    cols.add(j)
                    diag.add(j-i)
                    off_diag.add(j+i)
                    board.append("."*(j)+"Q"+"."*(n-j-1))
                    backtrack(i+1)
                    board.pop()
                    off_diag.remove(j+i)
                    diag.remove(j-i)
                    cols.remove(j)
        res = []
        board = []
        cols = set()
        diag = set()
        off_diag = set()
        backtrack(0)
        return res
'''
Example 1:

Input: n = 1
Output: [["Q"]]
--------------------
Example 2:

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
'''
