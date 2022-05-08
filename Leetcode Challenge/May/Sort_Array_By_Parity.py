'''
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ev=0
        odd=len(nums)-1
        while ev<odd:
            if nums[ev]%2!=0:
                nums[odd],nums[ev]=nums[ev],nums[odd]
                odd-=1

            else:
                ev+=1
        return nums
        
'''
--------------------------
Test Case 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]

Note:[4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
--------------------------
Test Case 2:

Input: nums = [0]
Output: [0]
'''
