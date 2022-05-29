'''
STATEMENT:
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
------------------------------------------------------------------------
'''
class Solution:
    def uniquePathsWithObstacles(self, M: List[List[int]]) -> int:
        m, n = len(M), len(M[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = int(M[0][0] == 0)
        for i, j in product(range(m), range(n)):
            if M[i][j] == 1: continue
            if i > 0: dp[i][j] += dp[i-1][j]
            if j > 0: dp[i][j] += dp[i][j-1]
                
        return dp[-1][-1]
     
'''
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''
