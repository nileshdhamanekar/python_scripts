# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Resource: https://www.youtube.com/watch?v=mj7N8pLCJ6w
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float('Infinity')
        max_val = 0
        for i in range(0, len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]
            else:
                max_val = max(max_val, prices[i] - min_val)
        return max_val