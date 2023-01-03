# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# Brute Force
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            for j in range(i+1,len(prices)):
                max_profit = max(max_profit,prices[j] - prices[i])
        return max_profit

# Finding the peak
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 100000
        max_profit = 0
        for i in range(len(prices)):
            min_price = min(min_price,prices[i])
            max_profit = max(max_profit,prices[i] - min_price)
        return max_profit

'''
Set minimal price to a high number, max profit to 0. For all prices, minimum price if min_price = prices[i]. 
Overwrite max profit if prices[i] - min_price > max_profit
'''