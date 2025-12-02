# https://leetcode.com/problems/coin-change/submissions/
# Resource (Dynamic Programming): https://www.youtube.com/watch?v=H9bfqozjoqs

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('Inf')] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0: 
                    dp[i] = min(dp[i], 1 + dp[i-coin])
        if dp[amount] != float('Inf'):
            return dp[amount]
        else:
            return -1