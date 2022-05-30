'''
STATEMENT:
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
--------------------------------------------------------
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        coins.sort()
        dp = [math.inf] * (amount+1)
        dp[0] = 0
        
        for amnt in range(1, amount+1):
            for coin in coins:
                if amnt >= coin:
                    dp[amnt] = min(dp[amnt], dp[amnt-coin] + 1)
                else:
                    break  # optimize a bit
                    
        return dp[amount] if dp[amount] != math.inf else -1
      
'''
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
-----------------
Input: coins = [2], amount = 3
Output: -1
---------------------------------
'''
