'''
STATEMENT:
You are given a string num representing a large integer. An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.
---------------------------------------------------------------------------------------------
'''
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l=len(num)
        if l<3:
            return ""
        li=[]
        for i in range(len(num)):
            ele=num[i]
            if len(li)==0 or li[-1][0]!=ele:
                li.append([ele,1])
                #   print(li[-1][1])

            else:
                li[-1][1]+=1
                #print(li[-1][1])

        ans=[]
        for k in li:
            if int(k[1])>=3:
                ans.append(str(k[0]*3))

        if len(ans)==0:
            return ""
        return max(ans)
'''
Input: num = "2300019"
Output: "000"
Explanation: "000" is the only good integer.
'''
