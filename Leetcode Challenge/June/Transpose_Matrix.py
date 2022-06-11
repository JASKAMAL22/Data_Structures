'''
STATEMENT:
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
----------------------------------------------------------
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109
--------------------------------------------------------------------------------
'''

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        mat=[]
        m,n=len(matrix),len(matrix[0])
        for j in range(n):
            k=[]
            for i in range(m):
                k.append(matrix[i][j])
               
            mat.append(k)
                
        return mat

'''
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
-----------------------
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
'''
