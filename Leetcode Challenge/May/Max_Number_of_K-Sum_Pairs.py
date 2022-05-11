class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c=0
        nums.sort()
        s=0
        e=len(nums)-1
        ans=0
        while s<e:
            ans=nums[s]+nums[e]
            if ans==k:
                c+=1
                s+=1
                e-=1
            elif ans>k:
                e-=1
            else:
                s+=1
        
        return c
'''
Test Case 1:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
-------------------------------
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
'''
