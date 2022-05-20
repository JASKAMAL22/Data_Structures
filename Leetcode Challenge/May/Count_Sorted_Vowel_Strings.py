'''
STATEMENT:
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.
-------------------------------------------------------------
'''
class Solution:
    def countVowelStrings(self, n: int) -> int:
        ans=0
        for i in range(1,n+2):
            s=0
            for j in range(1,i+1):
                s+=j
                ans+=s
                
        return ans
      
'''
-------------------------------------------------------------
Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet
'''
