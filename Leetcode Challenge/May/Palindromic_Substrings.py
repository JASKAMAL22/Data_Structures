'''
STATEMENT:
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
-----------------------------------------
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        l=len(s)
        c=0
        for i in range(l):
            j=l-1
            while j>=i:
                #print(i,j)
                sub=s[i:j+1]
                sub_rev=sub[-1::-1]
                #print(sub_rev)
                if sub==sub_rev:
                    c+=1
                j-=1

        return c
'''
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
--------------------------------
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''
