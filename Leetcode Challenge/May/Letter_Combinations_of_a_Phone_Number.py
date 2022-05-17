'''
STATEMENT:
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
--------------------------------------------------------------------------------------------------
'''

L = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}

class Solution:
    def letterCombinations(self, D: str) -> List[str]:
        lenD, ans = len(D), []
        if D == "": return []
        def bfs(pos: int, st: str):
            if pos == lenD: ans.append(st)
            else:
                letters = L[D[pos]]
                for letter in letters:
                    bfs(pos+1,st+letter)
        bfs(0,"")
        return 
'''
Test case 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
--------------------
Test case 2:
Input: digits = "2"
Output: ["a","b","c"]
'''
