'''
STATEMENT:
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false
--------------------------------------------------------------------------------------------------
'''
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
    
        if len(set(nums)) < 3:
            return False

        min_nums = [nums[0]]
        for i in range(1, len(nums)):
            min_nums.append(min(nums[i], min_nums[-1]))
            
        stack = []  
        i = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if( nums[i] > min_nums[i] ):
              
                while( stack and stack[-1] <= min_nums[i] ):
                    stack.pop()
                
                if(stack and min_nums[i] < stack[-1] < nums[i] ):
                    return True
               
                stack.append(nums[i])
        return False 
      
'''
Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
'''
