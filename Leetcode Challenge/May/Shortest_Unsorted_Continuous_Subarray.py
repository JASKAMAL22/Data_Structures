class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        i=0
        low,high=0,len(nums)-1
        while i<len(nums)-1:
            if nums[i]>nums[i+1]:
                low=i
                break
            i+=1
        j=len(nums)-1
        while j>0:
            if nums[j-1]>nums[j]:
                high=j
                break
            j-=1
        if low==len(nums)-1 or sorted(nums)==nums:
            return 0

        maxi=max(nums[low:high+1])
        mini=min(nums[low:high+1])

        while low-1>=0 and nums[low-1]>mini:
            low-=1
        
        while high+1<=len(nums)-1 and nums[high+1]<maxi:
            high+=1
    
        return high-low+1
    
'''
Test Case 1:
Input: nums = [1]
Output: 0

Test Case 2:
Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
'''
