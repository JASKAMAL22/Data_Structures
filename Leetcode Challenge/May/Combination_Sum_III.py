'''
STATEMENT:
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
------------------------------------------------------------------------------
'''

class Solution:
    def combinationSum3(self, k, n):
        self.sol = []
        self.BackTr(k, n, [])
        return self.sol
        
    def BackTr(self, k, n, curr_sol):
        if n < 0 or k < 0: return
        if n == 0 and k == 0:
            self.sol.append(curr_sol)
            
        start = curr_sol[-1] + 1 if curr_sol else 1
            
        for i in range(start, 10):
            self.BackTr(k - 1, n - i, curr_sol + [i])
           
'''
-------------------------------------------------------------------------------
TEST CASE:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations. '''
