'''
STATEMENT:
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
-----------------------------------------------------
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for level in range(1, len(triangle)):
            for i in range(level+1):
                triangle[level][i] += min(triangle[level-1][min(i, level-1)], triangle[level-1][max(i-1,0)])
        return min(triangle[-1])
      
      
'''
Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
--------------------------------------------
Example 2:

Input: triangle = [[-10]]
Output: -10
'''
