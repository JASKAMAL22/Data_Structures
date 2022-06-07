'''
STATEMENT:
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.
-------------------------------------------
'''
class Solution:
    def notsim(self,w1,w2):
        for ele in w2:
            if ele in w1:
                return False
        return True
    
    def maxProduct(self, words: List[str]) -> int:
        li=sorted(words,key=lambda x:len(x),reverse=True)
        l=len(li)
        ans=[0]
        #print(li)
        for i in range(l):
            j=i+1
            w1=li[i]
            while j<l:
                w2=li[j]
                if self.notsim(w1,w2):
                    mul=len(w1)*len(w2)
                    ans.append(mul)
                j+=1
                
        return max(ans)
      
'''
Example 1:

Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
-----------------------------
Example 2:

Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.
'''
