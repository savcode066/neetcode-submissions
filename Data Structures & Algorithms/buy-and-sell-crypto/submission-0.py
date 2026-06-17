class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = 0 
        sell = 1
        max_profit = 0

        for i in range(n-1):
            profit = prices[sell] - prices[buy]
            if profit < 0:
                buy = sell
            max_profit = max(profit, max_profit)
            sell += 1
        return max_profit
            

            



