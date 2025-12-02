# Resource: https://www.youtube.com/watch?v=blUwDD6JYaE
# The solution is correct not because you are selling on the days which are higher than the previous day 
# but rather the loop adds up all potential gains. So if for example the array is  [5, 7, 100]
# the best is to buy on day 1 where the price is 5 and sell on day three where the price is 100.   
# Kevin's solution adds the gains of day one to day two with the gains of day two to day three.  
# Even if selling and re buying on the same day is not allowed this is still correct.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == None or len(prices) == 0:
            return 0
        max_profit = 0
        for i in range(0, len(prices)-1):
            if prices[i] < prices[i+1]:
                max_profit += prices[i+1] - prices[i]
        return max_profit