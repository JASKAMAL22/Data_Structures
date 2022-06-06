'''
STATEMENT:
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
-------------------------------------------------
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=len(nums)
        s=0    
        for i in range(l+1):
            s+=i
            
        return s-sum(nums)
'''
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
'''
