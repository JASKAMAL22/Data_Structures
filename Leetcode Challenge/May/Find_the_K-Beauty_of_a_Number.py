'''
STATEMENT:
The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:

It has a length of k.
It is a divisor of num.
Given integers num and k, return the k-beauty of num.
--------------------------------------------------------------------

'''
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        n=num
        c=0
        num=str(num)
        for i in range(len(num)-k+1):
            j=i+k
            div=int(num[i:j])
            if div!=0 and n % div == 0:
                c+=1
        return c
        
'''
Input: num = 430043, k = 2
Output: 2
Explanation: The following are the substrings of num of length k:
-> "43" from "430043": 43 is a divisor of 430043.
-> "30" from "430043": 30 is not a divisor of 430043.
-> "00" from "430043": 0 is not a divisor of 430043.
-> "04" from "430043": 4 is not a divisor of 430043.
-> "43" from "430043": 43 is a divisor of 430043.
Therefore, the k-beauty is 2.
'''
