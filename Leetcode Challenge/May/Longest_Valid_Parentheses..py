'''
STATEMENT:
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
--------------------------------
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        dp, stack = [0]*(len(s) + 1), []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    p = stack.pop()
                    dp[i + 1] = dp[p] + i - p + 1
        return max(dp)


'''
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
---------------------------
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
----------------------------
'''
