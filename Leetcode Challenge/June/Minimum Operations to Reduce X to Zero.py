'''
STATEMENT:
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.
'''
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)

        leftMap = dict()
        leftMap[0] = -1
        left = 0
        for i in range(n):
            left += nums[i]
            if left not in leftMap:
                leftMap[left] = i

        right = 0
        ans = n + 1
        for i in range(n, -1, -1):
            if i < n:  right += nums[i]
            left = x - right
            if left in leftMap:  # left + right = x -> left = x - right
                ans = min(ans, leftMap[left] + 1 + n - i)
        if ans == n + 1: return -1
        return ans
      
 '''
 Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
'''
