class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        l=len(s)
        if l<k:
            return s
        li=[]
        for i in range(len(s)):
            ele=s[i]
            if len(li)==0 or li[-1][0]!=ele:
                li.append([ele,1])

            else:
                li[-1][1]+=1
                #print(li[-1][1])

            if int(li[-1][1])==k:
                li.pop()

        ans=""
        for k in li:
            ans+=k[0]*k[1]
    
        return ans
  '''
Input: s = "abcd", k = 2
Output: "abcd"
-----------------
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
'''
